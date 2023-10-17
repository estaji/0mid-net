import logging
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from scan.models import Job

logger = logging.getLogger(__name__)


def rm_jobs(threshold):
    """Get a threshold in days and remove all jobs older than the threshold"""
    time_threshold = timezone.now() - timedelta(days=threshold)
    old_jobs = Job.objects.filter(update_time__lte=time_threshold)
    for i in old_jobs:
        with transaction.atomic():
            i.delete()


def main():
    threshold_days = 10
    rm_jobs(threshold_days)
    logger.info("rm_old_jobs finished")


class Command(BaseCommand):
    help = "Old jobs remover"

    def handle(self, *args, **kwargs):
        main()
