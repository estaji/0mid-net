from django.db import models
from django.db.models import F


class Job(models.Model):
    """Jobs save in this model"""
    title = models.CharField(max_length=50, verbose_name='Job Title')
    company = models.CharField(max_length=50, verbose_name='Company Name')
    logo = models.ImageField(
        upload_to='company_logos/',
        verbose_name='Company Logo',
    )
    url = models.URLField(
        max_length=50,
        default='https://#',
        verbose_name='Company URL',
    )
    company_details = models.TextField(verbose_name='Company Description')
    start = models.DateField(verbose_name='Start Date')
    end = models.DateField(blank=True, null=True, verbose_name='End Date')
    location = models.CharField(max_length=50, verbose_name='Location/Remote')
    summary = models.TextField(verbose_name='Job Description')

    def __str__(self):
        return self.title+' at '+self.company

    class Meta:
        ordering = [F('end').desc(nulls_first=True)]


class Education(models.Model):
    """Add academic education in this model"""
    university = models.CharField(
        max_length=50,
        verbose_name='University Name',
    )
    level = models.CharField(max_length=20, verbose_name='Education Level')
    title = models.CharField(max_length=50, verbose_name='Field of Study')
    description = models.TextField(verbose_name='Description')
    start = models.DateField(verbose_name='Start Date')
    end = models.DateField(blank=True, null=True, verbose_name='End Date')

    def __str__(self):
        return self.title

    class Meta:
        ordering = [F('end').desc(nulls_first=True)]
