from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import F

from .utils import month_year_end, month_year_start, year_end, year_start


class Job(models.Model):
    """Jobs model"""

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
    """Academic educations model"""

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


class TechSkill(models.Model):
    """Technical Skills model for accordion style"""

    title = models.CharField(max_length=200, verbose_name="Technical Skill")
    certs = models.CharField(
        blank=True,
        max_length=100,
        verbose_name="Certification(s)",
    )
    details = models.TextField(blank=True, verbose_name="Description")
    order = models.IntegerField(unique=True, verbose_name="Order Number")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]


class TechSkillText(models.Model):
    """Technical Skills model for text style"""

    content = RichTextField(verbose_name="Content")


class SoftSkill(models.Model):
    """Soft Skills model"""

    title = models.CharField(max_length=100, verbose_name="Soft Skill")
    order = models.IntegerField(unique=True, verbose_name="Order Number")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]


class Language(models.Model):
    """Languages model"""

    title = models.CharField(max_length=50, verbose_name="Language")
    level = models.CharField(max_length=100, verbose_name="Proficiency")
    order = models.IntegerField(unique=True, verbose_name="Order Number")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]


class Jumbotron(models.Model):
    """Get Jumbotron information of website"""

    greeting = models.CharField(
        max_length=50, blank=True, verbose_name="Welcome Message"
    )
    title = models.CharField(max_length=50, verbose_name="Title/Name")
    occupation = models.CharField(max_length=100, blank=True, verbose_name="Job Titles")
    description = models.TextField(verbose_name="Description")
    email = models.EmailField(max_length=254, verbose_name="Email")
    picture = models.ImageField(
        upload_to="jumbotron_picture/",
        verbose_name="Picture/Avatar",
    )

    def __str__(self):
        return self.title


class SocialAccount(models.Model):
    """Social Accounts Model"""

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
    twitter = models.URLField(
        max_length=200,
        default="#",
        blank=True,
        verbose_name="Twitter Account",
    )


class ResumeConfig(models.Model):
    """Seo related tags and other configurations model for resume app"""

    SKILL_STYLE = [
        ("a", "accordion style"),
        ("t", "text style"),
    ]

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
        verbose_name="Open graph and Twitter card title",
    )
    twitter_user = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Twitter username for Twitter site tag",
    )
    skills_style = models.CharField(
        max_length=1,
        choices=SKILL_STYLE,
        default="a",
        verbose_name="Skills section style",
    )
