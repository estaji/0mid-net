from django.db import models
from django.utils import timezone
from core.models import User
from blog.utils import published_date, date_ymd
from ckeditor.fields import RichTextField


class ArticleManager(models.Manager):
    """Return published articles"""
    def published(self):
        return self.filter(status='p')


class Tag(models.Model):
    ''''Model for Tags'''
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='Slug/URL',
    )
    position = models.IntegerField(unique=True, verbose_name='Position')
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='Meta description tag',
    )
    keywords = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Meta keywords tag',
    )
    robots = models.CharField(
        max_length=60,
        blank=True,
        verbose_name='Meta robots tag',
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['position']

    def __str__(self):
        return self.title

    def posts_count(self):
        """Count number of posts for a tag"""
        return Article.objects.filter(tag=self, status='p').count()


class Article(models.Model):
    """Model for blog's post"""
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
    ]
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('fa', 'Persian'),
    ]
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='articles',
        verbose_name="Author",
    )
    title = models.CharField(max_length=250, verbose_name="Title")
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name="Slug/URL",
    )
    tag = models.ManyToManyField(
        Tag,
        related_name="articles",
        verbose_name="Tag",
    )
    subheading = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Subheading",
    )
    content = RichTextField(verbose_name="Content")
    published = models.DateField(
        default=timezone.now,
        verbose_name="Published on",
    )
    created = models.DateField(
        auto_now_add=True,
        verbose_name="Created on",
    )
    updated = models.DateField(auto_now=True, verbose_name="Updated on")
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        verbose_name="Status",
    )
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        verbose_name="Language",
    )
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='Meta description tag',
    )
    keywords = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Meta keywords tag',
    )
    robots = models.CharField(
        max_length=60,
        blank=True,
        verbose_name='Meta robots tag',
    )

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-published']

    def __str__(self):
        return self.title

    def published_modified(self):
        """return published date as Today,or x days before or year-month-day"""
        published = published_date(self.published)
        return published

    def published_ymd(self):
        """return published date as year-month-day"""
        return date_ymd(self.published)

    def create_ymd(self):
        """return create date as year-month-day"""
        return date_ymd(self.created)

    def update_ymd(self):
        """return update/modified date as year-month-day"""
        return date_ymd(self.updated)

    def article_tags(self):
        """Get all tags for an article"""
        return ",\n".join([p.title for p in self.tag.all()])

    objects = ArticleManager()


class Configuration(models.Model):
    """Blog configurations model"""
    copyr = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Copyright message in footer',
    )
    email = models.EmailField(max_length=254, verbose_name='Email')
    linkedin = models.URLField(
        max_length=200,
        default="#",
        blank=True,
        verbose_name='Linkedin Account',
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Title in menu bar',
        default='Blog Name',
    )
    title = models.CharField(
        max_length=70,
        verbose_name="Title in main page",
        default='Blog Title',
    )
    subtitle = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Sub-title in main page',
    )
    meta_author = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Meta author tag',
    )
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='Meta description tag',
    )
    keywords = models.CharField(
        max_length=160,
        blank=True,
        verbose_name='Meta keywords tag',
    )
    robots = models.CharField(
        max_length=60,
        blank=True,
        verbose_name='Meta robots tag',
    )
