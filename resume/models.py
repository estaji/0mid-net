from django.db import models
from django.db.models import F


class Job(models.Model):
    """Jobs model"""
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
    company_details = models.TextField(
        blank=True,
        verbose_name='Company Description',
    )
    start = models.DateField(verbose_name='Start Date')
    end = models.DateField(blank=True, null=True, verbose_name='End Date')
    location = models.CharField(
        blank=True,
        max_length=50,
        verbose_name='Location/Remote',
    )
    summary = models.TextField(blank=True, verbose_name='Job Description')

    def __str__(self):
        return self.title+' at '+self.company

    class Meta:
        ordering = [F('end').desc(nulls_first=True)]


class Education(models.Model):
    """Academic educations model"""
    university = models.CharField(
        max_length=50,
        verbose_name='University Name',
    )
    level = models.CharField(
        blank=True,
        max_length=20,
        verbose_name='Education Level',
    )
    title = models.CharField(max_length=50, verbose_name='Field of Study')
    description = models.TextField(blank=True, verbose_name='Description')
    start = models.DateField(verbose_name='Start Date')
    end = models.DateField(blank=True, null=True, verbose_name='End Date')

    def __str__(self):
        return self.title

    class Meta:
        ordering = [F('end').desc(nulls_first=True)]


class TechSkill(models.Model):
    """Technical Skills model"""
    title = models.CharField(max_length=200, verbose_name='Technical Skill')
    certs = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Certification(s)',
    )
    details = models.TextField(blank=True, verbose_name='Description')
    order = models.IntegerField(unique=True, verbose_name='Order Number')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class SoftSkill(models.Model):
    """Soft Skills model"""
    title = models.CharField(max_length=50, verbose_name='Soft Skill')
    details = models.TextField(blank=True, verbose_name='Description')
    order = models.IntegerField(unique=True, verbose_name='Order Number')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Language(models.Model):
    """Languages model"""
    title = models.CharField(max_length=50, verbose_name='Language')
    level = models.CharField(max_length=100, verbose_name='Proficiency')
    order = models.IntegerField(unique=True, verbose_name='Order Number')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Jumbotron(models.Model):
    """Get Jumbotron information of website"""
    greeting = models.CharField(max_length=50, verbose_name='Welcome Message')
    title = models.CharField(max_length=50, verbose_name='Title/Name')
    description = models.TextField(verbose_name='Description')
    email = models.EmailField(max_length=254, verbose_name='Email')
    picture = models.ImageField(
        upload_to='jumbotron_picture/',
        verbose_name='Picture/Avatar',
    )

    def __str__(self):
        return self.title
