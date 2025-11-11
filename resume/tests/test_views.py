import tempfile
from datetime import date

from django.test import TestCase
from django.urls import reverse

from resume.models import (
    Education,
    Job,
    Jumbotron,
    Language,
    Configuration,
    SocialAccount,
    TechSkill,
)


class ResumeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Configuration.objects.create(
            email="me@test.com",
            site_title="My site",
            title="My full name",
            description="This is my personal website",
            robots="follow",
            author="Mr Test",
            keywords="personal blog, tag",
            favicon=tempfile.NamedTemporaryFile(suffix=".png").name,
            og_title="My OpenGraph title",
            xcom_user="username",
        )
        Job.objects.create(
            title="Software Engineer",
            company="Google",
            url="https://google.com",
            company_details="An enterprise company",
            start=date.today(),
            end=None,
            location="USA",
            summary="Lead all tech departments",
        )
        Education.objects.create(
            university="Stanford",
            level="PhD",
            title="Computer Security",
            description="protection of computer systems",
            start=date.today(),
            end=None,
        )
        TechSkill.objects.create(content="Linux servers and CloudLinux")
        Language.objects.create(
            title="English",
            level="IELTS 9",
            order=3,
        )
        Jumbotron.objects.create(
            greeting="Welcome to my site",
            title="My full name",
            occupation="SysOps Engineer",
            description="This is my personal website",
            picture=tempfile.NamedTemporaryFile(suffix=".jpg").name,
        )
        SocialAccount.objects.create(
            linkedin="https://www.linkedin.com/in/acc",
            github="https://github.com/acc",
            stackexchange="https://stackexchange.com/users/acc",
            instagram="",
            xcom="https://twitter.com/acc",
        )

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location"""
        response = self.client.get("")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by app:urlname"""
        response = self.client.get(reverse("resume"))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template"""
        response = self.client.get(reverse("resume"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "resume/resume.html")

    def test_view_skill_section(self):
        """Test view and webpage contains the text in tech skill text style"""
        response = self.client.get(reverse("resume"))

        self.assertContains(response, "Linux servers and CloudLinux")

    def test_view_jumbotron_items(self):
        """Test view, jumbotron contains defined items"""
        response = self.client.get(reverse("resume"))

        self.assertContains(response, "SysOps Engineer")