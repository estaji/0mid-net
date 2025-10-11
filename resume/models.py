from django.db import models
from django.db.models import F

from .utils import month_year_end, month_year_start, year_end, year_start


class Jumbotron(models.Model):
    greeting = models.CharField(
        max_length=70, blank=True, verbose_name="Welcome Message"
    )
    title = models.CharField(max_length=70, verbose_name="Title/Name")
    occupation = models.CharField(max_length=120, blank=True, verbose_name="Job Titles")
    description = models.TextField(verbose_name="Description")
    email = models.EmailField(max_length=254, verbose_name="Email")
    picture = models.ImageField(
        upload_to="jumbotron_picture/",
        verbose_name="Picture/Avatar",
    )

    def __str__(self):
        return self.title


# class TechSkill(models.Model):


class Job(models.Model):
    title = models.CharField(max_length=50, verbose_name="Job Title")
    company = models.CharField(max_length=50, verbose_name="Company Name")
    logo = models.ImageField(
        blank=True,
        upload_to="company_logos/",
        verbose_name="Company Logo",
    )
    url = models.URLField(
        max_length=50,
        default="https://#",
        verbose_name="Company URL",
    )
    company_details = models.TextField(
        blank=True,
        verbose_name="Company Description",
    )
    start = models.DateField(verbose_name="Start Date")
    end = models.DateField(blank=True, null=True, verbose_name="End Date")
    location = models.CharField(
        blank=True,
        max_length=50,
        verbose_name="Location/Remote",
    )
    summary = models.TextField(blank=True, verbose_name="Job Description")

    def __str__(self):
        return self.title + " at " + self.company

    class Meta:
        ordering = [F("end").desc(nulls_first=True)]

    def short_start(self):
        return month_year_start(self.start)

    def modified_end(self):
        return month_year_end(self.end)


class Education(models.Model):
    university = models.CharField(
        max_length=50,
        verbose_name="University Name",
    )
    level = models.CharField(
        max_length=20,
        verbose_name="Education Level",
    )
    title = models.CharField(max_length=50, verbose_name="Field of Study")
    description = models.TextField(blank=True, verbose_name="Description")
    start = models.DateField(verbose_name="Start Date")
    end = models.DateField(blank=True, null=True, verbose_name="End Date")

    def __str__(self):
        return self.title

    class Meta:
        ordering = [F("end").desc(nulls_first=True)]

    def short_start(self):
        return year_start(self.start)

    def modified_end(self):
        new_end = year_end(self.end)
        return new_end


# class Recommendation(models.Model):


class Language(models.Model):
    title = models.CharField(max_length=50, verbose_name="Language")
    level = models.CharField(max_length=100, verbose_name="Proficiency")
    order = models.IntegerField(unique=True, verbose_name="Order Number")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]


class SocialAccount(models.Model):
    linkedin = models.URLField(
        max_length=200,
        default="#",
        blank=True,
        verbose_name="Linkedin Account",
    )
    github = models.URLField(
        max_length=200,
        default="#",
        blank=True,
        verbose_name="Github Account",
    )
    stackexchange = models.URLField(
        max_length=254,
        default="#",
        blank=True,
        verbose_name="Stackexchange Account",
    )
    instagram = models.URLField(
        max_length=200,
        default="#",
        blank=True,
        verbose_name="Instagram Account",
    )
    xcom = models.URLField(
        max_length=200,
        default="#",
        blank=True,
        verbose_name="X Account",
    )


class Configuration(models.Model):
    site_title = models.CharField(
        max_length=60,
        blank=True,
        verbose_name="Website title",
    )
    title = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="Title tag",
    )
    description = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="Meta description tag",
    )
    robots = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="Meta robots tag",
    )
    author = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="Meta author tag",
    )
    keywords = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="Meta keywords tag",
    )
    og_title = models.CharField(
        max_length=60,
        blank=True,
        verbose_name="Open graph and X card title",
    )
    xcom_user = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="X username for X site tag",
    )
