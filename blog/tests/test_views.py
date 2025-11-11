from datetime import date
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Article, Tag

User = get_user_model()

class BlogListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location for /blog/"""
        response = self.client.get("/blog/")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by blog:home"""
        response = self.client.get(reverse("blog:home"))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template for blog:home"""
        response = self.client.get(reverse("blog:home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/home.html")


class ArticleDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            title="Django",
            slug="django-tag",
            position=1,
            meta_description="test meta description string",
            keywords="tagkw1, tagkw2",
        )
        User.objects.create(
            email="testuser@gmail.com",
            is_active=True,
            is_staff=False,
        )

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location for /blog/<slug:slug>"""
        self.article1 = Article.objects.create(
            author=User.objects.get(email="testuser@gmail.com"),
            title="Class based views",
            slug="django-cb-views",
            subheading="Article about CBVs",
            content="this is a test for CBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="p",
            language="en",
        )
        self.article1.tag.add(Tag.objects.get(title="Django"))

        response = self.client.get("/blog/django-cb-views")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by blog:article and slug as kwargs"""
        self.article1 = Article.objects.create(
            author=User.objects.get(email="testuser@gmail.com"),
            title="Class based views",
            slug="django-cb-views",
            subheading="Article about CBVs",
            content="this is a test for CBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="p",
            language="en",
        )
        self.article1.tag.add(Tag.objects.get(title="Django"))

        response = self.client.get(
            reverse("blog:article", kwargs={"slug": "django-cb-views"})
        )

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template for blog:article"""
        self.article1 = Article.objects.create(
            author=User.objects.get(email="testuser@gmail.com"),
            title="Class based views",
            slug="django-cb-views",
            subheading="Article about CBVs",
            content="this is a test for CBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="p",
            language="en",
        )
        self.article1.tag.add(Tag.objects.get(title="Django"))

        response = self.client.get(
            reverse("blog:article", kwargs={"slug": "django-cb-views"})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/article.html")

    def test_view_only_show_published_articles(self):
        """Test view only show published articles"""
        self.article1 = Article.objects.create(
            author=User.objects.get(email="testuser@gmail.com"),
            title="Class based views",
            slug="django-cb-views",
            subheading="Article about CBVs",
            content="this is a test for CBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="p",
            language="en",
        )
        self.article1.tag.add(Tag.objects.get(title="Django"))
        self.article2 = Article.objects.create(
            author=User.objects.get(email="testuser@gmail.com"),
            title="Function based views",
            slug="django-fb-views",
            subheading="Article about FBVs",
            content="this is a test for FBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="d",
            language="en",
        )
        self.article2.tag.add(Tag.objects.get(title="Django"))

        response_published = self.client.get(
            reverse("blog:article", kwargs={"slug": "django-cb-views"})
        )
        response_drafted = self.client.get(
            reverse("blog:article", kwargs={"slug": "django-fb-views"})
        )

        self.assertEqual(response_published.status_code, 200)
        self.assertEqual(response_drafted.status_code, 404)


class TagListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            title="Django",
            slug="django",
            position=1,
            meta_description="test meta description string",
            keywords="tagkw1, tagkw2",
        )

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location for blog/tag/<slug:slug>"""
        response = self.client.get("/blog/tag/django")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by blog:tag and slug as kwargs"""
        response = self.client.get(reverse("blog:tag", kwargs={"slug": "django"}))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template for blog:tag"""
        response = self.client.get(reverse("blog:tag", kwargs={"slug": "django"}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/tag.html")


class AllTagsListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            title="Django",
            slug="django",
            position=1,
            meta_description="test meta description string",
            keywords="tagkw1, tagkw2",
        )
        Tag.objects.create(
            title="Linux",
            slug="linux",
            position=2,
            meta_description="test meta description string",
            keywords="tagkw1, tagkw2",
        )

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location for /blog/tags"""
        response = self.client.get("/blog/tags")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by blog:tagslist"""
        response = self.client.get(reverse("blog:tagslist"))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template for blog:tagslist"""
        response = self.client.get(reverse("blog:tagslist"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/tagslist.html")

    def test_view_contains_all_tags(self):
        """test view contains all tags in blog:tagslist"""
        response = self.client.get(reverse("blog:tagslist"))

        self.assertContains(
            response, "Django", count=None, status_code=200, msg_prefix="", html=False
        )
        self.assertContains(
            response, "Linux", count=None, status_code=200, msg_prefix="", html=False
        )


class ArticlePreviewDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            title="Django",
            slug="django-tag",
            position=1,
            meta_description="test meta description string",
            keywords="tagkw1, tagkw2",
        )
        User.objects.create(
            email="linustorvalds@gmail.com",
            password="P@ssw0rd",
            is_active=True,
            is_staff=True,
        )

    def test_requiredlogin_view_redirect302_to_desired_location(self):
        """Test preview view returns 302 redirect for logged out users"""
        self.article1 = Article.objects.create(
            author=User.objects.get(email="linustorvalds@gmail.com"),
            title="Class based views",
            slug="django-cb-views",
            subheading="Article about CBVs",
            content="this is a test for CBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="d",
            language="en",
        )
        self.article1.tag.add(Tag.objects.get(title="Django"))

        response = self.client.get("/blog/preview/django-cb-views")

        self.assertEqual(response.status_code, 302)

    def test_requiredlogin_view_return_200_to_logged_in_user(self):
        """Test preview view returns 200 to a logged in user
        Also Test view url exists at desired location
        for /blog/preview/<slug:slug>"""
        self.article1 = Article.objects.create(
            author=User.objects.get(email="linustorvalds@gmail.com"),
            title="Class based views",
            slug="django-cb-views",
            subheading="Article about CBVs",
            content="this is a test for CBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="d",
            language="en",
        )
        self.article1.tag.add(Tag.objects.get(title="Django"))

        self.client.force_login(User.objects.get(email="linustorvalds@gmail.com"))
        response = self.client.get("/blog/preview/django-cb-views")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by blog:preview"""
        self.article1 = Article.objects.create(
            author=User.objects.get(email="linustorvalds@gmail.com"),
            title="Class based views",
            slug="django-cb-views",
            subheading="Article about CBVs",
            content="this is a test for CBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="d",
            language="en",
        )
        self.article1.tag.add(Tag.objects.get(title="Django"))

        self.client.force_login(User.objects.get(email="linustorvalds@gmail.com"))
        response = self.client.get(
            reverse("blog:preview", kwargs={"slug": "django-cb-views"})
        )

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template for blog:preview"""
        self.article1 = Article.objects.create(
            author=User.objects.get(email="linustorvalds@gmail.com"),
            title="Class based views",
            slug="django-cb-views",
            subheading="Article about CBVs",
            content="this is a test for CBVs",
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status="d",
            language="en",
        )
        self.article1.tag.add(Tag.objects.get(title="Django"))

        self.client.force_login(User.objects.get(email="linustorvalds@gmail.com"))
        response = self.client.get(
            reverse("blog:preview", kwargs={"slug": "django-cb-views"})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/article.html")