import logging

# import urllib.request
# import json
import time
from datetime import timedelta
from threading import Lock, Thread

import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Q
from django.utils import timezone

from scan.models import Job, Node
from scan.utils import http_check, pinging, ssl_check

logger = logging.getLogger(__name__)


def check_old_jobs():
    """Check old jobs"""

    """Set very old jobs to failed"""
    time_threshold = timezone.now() - timedelta(days=1)
    old_jobs = Job.objects.filter(
        Q(status="n") | Q(status="r"), start_time__lte=time_threshold
    )
    for i in old_jobs:
        with transaction.atomic():
            i.status = "f"
            i.save()

    """Check current running jobs and set them to success or none"""
    runnings = Job.objects.filter(status="r")
    for i in runnings:
        if i.result != "":
            with transaction.atomic():
                i.status = "s"
                i.save()
        else:
            with transaction.atomic():
                i.status = "n"
                i.save()

    logger.info("old jobs checked successfuly")


def none_jobs_count():
    """Check is there any none job to do or not?"""
    try:
        count = Job.objects.filter(status="n").count()
        # logger.debug("there are {} none_jobs_count".format(count))
        return count
    except AttributeError:
        return False


def get_job():
    """Get oldest none job and set it to running and return it"""
    try:
        job = Job.objects.filter(status="n").order_by("add_time").first()
        with transaction.atomic():
            job.status = "r"
            job.save()
        return job
    except AttributeError:
        pass
    #    exit()


def do_job(job):
    """Get a job and set it to running and do it"""
    if job.command == "pi":
        nodes = Node.objects.filter(is_active=True)
        for i in nodes:
            with transaction.atomic():
                newjob = Job()
                newjob.start_time = timezone.now()
                newjob.command = "p"
                newjob.node = i
                newjob.uuid = job.uuid
                newjob.url = job.url
                newjob.save()
        with transaction.atomic():
            job.status = "s"
            job.save()
    elif job.command == "p":
        if job.node.node_type == "p":
            result = pinging(job.url)
            with transaction.atomic():
                job.result = result
                job.status = "s"
                job.save()
        else:
            nodes = Node.objects.filter(is_active=True, node_type="c")
            for i in nodes:
                url = "{}/scan/api/ping?url={}".format(i.url, job.url)
                headers = {"Authorization": "Token {}".format(i.token)}
                response = requests.get(url, headers=headers)
                data = response.json()
                # theurl = "{}/api/ping?url={}".format(i.url, job.url)
                # response = urllib.request.urlopen(theurl).read()
                # data = json.loads(response.decode('utf-8'))
                with transaction.atomic():
                    job.result = data["result"]
                    job.status = "s"
                    job.save()

    elif job.command == "hi":
        nodes = Node.objects.filter(is_active=True)
        for i in nodes:
            with transaction.atomic():
                newjob = Job()
                newjob.start_time = timezone.now()
                newjob.command = "h"
                newjob.node = i
                newjob.uuid = job.uuid
                newjob.url = job.url
                newjob.save()
        with transaction.atomic():
            job.status = "s"
            job.save()
    elif job.command == "h":
        if job.node.node_type == "p":
            result = http_check(job.url)
            with transaction.atomic():
                job.result = result
                job.status = "s"
                job.save()
        else:
            nodes = Node.objects.filter(is_active=True, node_type="c")
            for i in nodes:
                url = "{}/scan/api/http?url={}".format(i.url, job.url)
                headers = {"Authorization": "Token {}".format(i.token)}
                response = requests.get(url, headers=headers)
                data = response.json()
                with transaction.atomic():
                    job.result = data["result"]
                    job.status = "s"
                    job.save()
    elif job.command == "si":
        with transaction.atomic():
            newjob = Job()
            newjob.start_time = timezone.now()
            newjob.command = "s"
            newjob.node = Node.objects.filter(node_type="p").first()
            newjob.uuid = job.uuid
            newjob.url = job.url
            newjob.save()
            job.status = "s"
            job.save()
    elif job.command == "s":
        result = ssl_check(job.url)
        with transaction.atomic():
            job.result = result
            job.status = "s"
            job.save()


def main():
    logger.info("daemon started")
    check_old_jobs()
    while True:
        time.sleep(0.05)
        if none_jobs_count() != 0:
            mutex = Lock()
            for _ in range(none_jobs_count()):
                mutex.acquire()
                job = get_job()
                mutex.release()
                t_ = Thread(target=do_job, args=(job,))
                t_.start()
        time.sleep(0.05)


class Command(BaseCommand):
    help = "Daemon for doing jobs"

    def handle(self, *args, **kwargs):
        main()
