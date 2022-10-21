from django.db import models
from django.db.models import Q


class Node(models.Model):
    """Node model which stores information about a node such as type and etc"""
    TYPE_CHOICES = [
        ('c', 'Child'),
        ('p', 'Parent')
    ]

    node_type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        verbose_name='Node Type'
    )
    location = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Location'
    )
    url = models.URLField(
        max_length=50,
        default='https://#',
        unique=True,
        verbose_name='URL',
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Is active'
    )
    token = models.CharField(
        max_length=40,
        blank=True,
        verbose_name='Token'
    )

    def __str__(self):
        return self.location


class Job(models.Model):
    """Job model which stores information, duties and result of jobs"""
    COMMAND_CHOICES = [
        ('pi', 'ping instantly'),
        ('p', 'ping'),
    ]
    STATUS_CHOICES = [
        ('n', 'none'),
        ('r', 'running'),
        ('s', 'success'),
        ('f', 'failed'),
    ]

    id = models.AutoField(primary_key=True, verbose_name="Job id")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Add time")
    start_time = models.DateTimeField(verbose_name="Start time")
    update_time = models.DateTimeField(
        auto_now=True, verbose_name="Last update"
    )
    command = models.CharField(
        max_length=2,
        choices=COMMAND_CHOICES,
        verbose_name="Command type"
    )
    node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        verbose_name="Node"
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='n',
        verbose_name="Status"
    )
    uuid = models.UUIDField(verbose_name="UUID")
    url = models.URLField(
        max_length=300,
        blank=False,
        verbose_name='URL',
    )
    result = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Result"
    )

    def uuid_result_jobs(uuid):
        """Get a uuid and return jobs with final result(s) of the uuid"""
        result = Job.objects.filter(~Q(result="") & Q(status='s'), uuid=uuid)

        return result

    def uuid_children_count(uuid):
        """Get a uuid and return number of child/children jobs"""
        alljobs = Job.objects.filter(uuid=uuid).count()
        children = alljobs - 1

        return children

    def url_of_uuid(uuid):
        """Get a uuid and return url of it"""
        job = Job.objects.filter(uuid=uuid).latest('add_time')

        return job.url


class ScanConfig(models.Model):
    """Seo related tags and other configurations model"""
    title = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='Title tag',
    )
    description = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='Meta description tag',
    )
    keywords = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='Meta keywords tag',
    )
