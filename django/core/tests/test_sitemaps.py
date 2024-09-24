from datetime import date, datetime, timedelta

from django.test import TestCase
from django.urls import reverse

from blog.models import Article, Tag
from core.models import User


class SitemapsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            title="Linux",
            slug="linux",
            position=1,
            meta_description="useful and fresh articles about Linux",
            keywords="Linux, RedHat, Debian",
        )
        User.objects.create(
            email="linustorvalds@gmail.com",
            name="Linus Torvalds",
            is_active=True,
            is_staff=False,
        )

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location for /sitemap.xml/"""
        response = self.client.get("/sitemap.xml")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by django.contrib.sitemaps.views.sitemap"""
        response = self.client.get(reverse("django.contrib.sitemaps.views.sitemap"))

        self.assertEqual(response.status_code, 200)

    def test_sitemap_contains_blog_homepage(self):
        """Test sitemap contains blog hompage at /blog"""
        response = self.client.get("/sitemap.xml")

        self.assertContains(
            response, "/blog", count=None, status_code=200, msg_prefix="", html=False
        )

    def test_sitemap_contains_blog_tags_page(self):
        """Test sitemap contains blog tags page at /blog/tags"""
        response = self.client.get("/sitemap.xml")

        self.assertContains(
            response,
            "/blog/tags",
            count=None,
            status_code=200,
            msg_prefix="",
            html=False,
        )

    def test_sitemap_contains_created_tag(self):
        """Test sitemap contains created tag - /blog/tag/<tag_slug>"""
        response = self.client.get("/sitemap.xml")

        self.assertContains(
            response,
            "/blog/tag/{}".format(Tag.objects.get(slug="linux").slug),
            count=None,
            status_code=200,
            msg_prefix="",
            html=False,
        )

    def test_sitemap_contains_created_article(self):
        """Test sitemap contains created article - /blog/<article_slug>"""
        self.article = Article.objects.create(
            author=User.objects.get(email="linustorvalds@gmail.com"),
            title="fdisk tool",
            slug="fdisk",
            subheading="Manage Linux disk using fdisk",
            content="this is a test for fdisk article",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="p",
            language="en",
        )
        self.article.tag.add(Tag.objects.get(title="Linux"))
        response = self.client.get("/sitemap.xml")

        self.assertContains(
            response,
            "/blog/{}".format(self.article.slug),
            count=None,
            status_code=200,
            msg_prefix="",
            html=False,
        )

    def test_sitemap_does_not_contain_drafted_article(self):
        """Test sitemap doesn't contain drafted article"""
        self.article = Article.objects.create(
            author=User.objects.get(email="linustorvalds@gmail.com"),
            title="fdisk tool",
            slug="fdisk",
            subheading="Manage Linux disk using fdisk",
            content="this is a test for fdisk article",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="d",
            language="en",
        )
        self.article.tag.add(Tag.objects.get(title="Linux"))
        response = self.client.get("/sitemap.xml")

        self.assertNotContains(
            response,
            "/blog/{}".format(self.article.slug),
            status_code=200,
            msg_prefix="",
            html=False,
        )

    def test_sitemap_shows_lastmod_of_article_correctly(self):
        """Test sitemap shows lastmod of article correctly"""
        twodaysago = datetime.strftime(datetime.now() - timedelta(2), "%Y-%m-%d")
        self.article = Article.objects.create(
            author=User.objects.get(email="linustorvalds@gmail.com"),
            title="fdisk tool",
            slug="fdisk",
            subheading="Manage Linux disk using fdisk",
            content="this is a test for fdisk article",
            published=twodaysago,
            created=twodaysago,
            updated=date.today(),
            status="p",
            language="en",
        )
        self.article.tag.add(Tag.objects.get(title="Linux"))
        response = self.client.get("/sitemap.xml")

        self.assertContains(
            response,
            "<lastmod>{}</lastmod>".format(date.today()),
            count=None,
            status_code=200,
            msg_prefix="",
            html=False,
        )
