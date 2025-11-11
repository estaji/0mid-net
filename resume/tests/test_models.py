from django.contrib.auth import get_user_model
from datetime import date
from django.test import TestCase

from resume.models import (
    Menu,
    SubMenu,
    Configuration,
    SocialAccount,
    Language,
    Recommendation,
    Education,
    Job,
    TechSkill,
    Jumbotron,
)


class JumbotronModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Jumbotron.objects.create(
            greeting="Welcome to my site",
            title="My full name",
            occupation="An Engineer",
            description="This is my personal website",
        )

    def test_add_jumbotron(self):
        """Test add a jumbotron"""
        item = Jumbotron.objects.get(id=1)

        self.assertEqual(item.greeting, "Welcome to my site")
        self.assertEqual(item.title, "My full name")
        self.assertEqual(item.occupation, "An Engineer")
        self.assertEqual(item.description, "This is my personal website")

class TechSkillTextModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        TechSkill.objects.create(
            content="A Simple Content",
        )

    def test_add_techskill(self):
        """Test add a technical skill in text style"""
        item = TechSkill.objects.get(id=1)

        self.assertEqual(item.content, "A Simple Content")

class JobModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
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
        Job.objects.create(start=date.today(), end=date.today())

    def test_short_start_month_year(self):
        """Test start date show month and year"""
        item = Job.objects.get(id=1)
        date1 = Job.short_start(item)
        for_date2 = item.start
        date2 = for_date2.strftime("%B %Y")

        self.assertEqual(date1, date2)

    def test_modified_end_month_year_present(self):
        """Test job end field returns PRESENT when is empty"""
        item = Job.objects.get(id=1)
        end_field = Job.modified_end(item)

        self.assertEqual(end_field, "Present")

    def test_modified_end_month_year(self):
        """Test job end field returns modified date when is NOT empty"""
        item = Job.objects.get(id=2)
        date1 = Job.modified_end(item)
        for_date2 = item.end
        date2 = for_date2.strftime("%B %Y")

        self.assertEqual(date1, date2)

    def test_add_job(self):
        """Test add a job"""
        item = Job.objects.get(id=1)

        self.assertEqual(item.title, "Software Engineer")
        self.assertEqual(item.company, "Google")
        self.assertURLEqual(item.url, "https://google.com")
        self.assertEqual(item.company_details, "An enterprise company")
        self.assertEqual(item.location, "USA")
        self.assertEqual(item.summary, "Lead all tech departments")

class EducationModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Education.objects.create(
            university="Stanford",
            level="PhD",
            title="Computer Security",
            description="protection of computer systems",
            start=date.today(),
            end=None,
        )
        Education.objects.create(start=date.today(), end=date.today())

    def test_add_education(self):
        """Test add a education"""
        item = Education.objects.get(id=1)

        self.assertEqual(item.title, "Computer Security")
        self.assertEqual(item.university, "Stanford")
        self.assertEqual(item.level, "PhD")
        self.assertEqual(item.description, "protection of computer systems")

    def test_short_start_year(self):
        """Test education start date shows year"""
        item = Education.objects.get(id=1)
        date1 = Education.short_start(item)
        for_date2 = item.start
        date2 = for_date2.strftime("%Y")

        self.assertEqual(date1, date2)

    def test_modified_end_year_present(self):
        """Test education end field returns PRESENT when is empty"""
        item = Education.objects.get(id=1)
        end_field = Education.modified_end(item)

        self.assertEqual(end_field, "Present")

    def test_modified_end_year(self):
        """Test education end field returns modified date when is NOT empty"""
        item = Education.objects.get(id=2)
        date1 = Education.modified_end(item)
        for_date2 = item.end
        date2 = for_date2.strftime("%Y")

        self.assertEqual(date1, date2)

class RecommendationModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Recommendation.objects.create(
            author_name="Jadi",
            author_title="Software Engineer",
            date_received=date.today(),
            content="Omid is a nice dude",
            order=1,
        )

    def test_add_recommendation(self):
        """Test add a recommendation"""
        item = Recommendation.objects.get(id=1)

        self.assertEqual(item.author_name, "Jadi")
        self.assertEqual(item.author_title, "Software Engineer")
        self.assertEqual(item.date_received, date.today())
        self.assertEqual(item.content, "Omid is a nice dude")
        self.assertEqual(item.order, 1)

class LanguageModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(
            title="English",
            level="IELTS 9",
            order=3,
        )

    def test_add_language(self):
        """Test add a language"""
        item = Language.objects.get(id=1)

        self.assertEqual(item.title, "English")
        self.assertEqual(item.level, "IELTS 9")
        self.assertEqual(item.order, 3)

class SocialAccountModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        SocialAccount.objects.create(
            linkedin="https://www.linkedin.com/in/acc",
            github="https://github.com/acc",
            stackexchange="https://stackexchange.com/users/acc",
            instagram="",
            xcom="https://twitter.com/acc",
        )

    def test_add_socialaccount(self):
        """Test add a social account object"""
        item = SocialAccount.objects.get(id=1)

        self.assertURLEqual(
            item.linkedin,
            "https://www.linkedin.com/in/acc",
        )
        self.assertURLEqual(item.github, "https://github.com/acc")
        self.assertURLEqual(
            item.stackexchange,
            "https://stackexchange.com/users/acc",
        )
        self.assertURLEqual(item.instagram, "")
        self.assertURLEqual(item.xcom, "https://twitter.com/acc")

class ConfigModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Configuration.objects.create(
            email="myaccount@gmail.com",
            site_title="My CV",
            title="This is title",
        )

    def test_add_configuration(self):
        """Test add a configuration"""
        item = Configuration.objects.get(id=1)

        self.assertEqual(item.email, "myaccount@gmail.com")
        self.assertEqual(item.site_title, "My CV")
        self.assertEqual(item.title, "This is title")

class MenuModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(
            title="Blog",
            url="https://blog.test.org",
            order="2",
            icon_type="N",
        )

    def test_add_menu_item(self):
        """Test add an item to menu"""
        item = Menu.objects.get(id=1)

        self.assertEqual(item.url, "https://blog.test.org")

    def test_add_submenu(self):
        """Test add a submenu"""
        menu_item = Menu.objects.get(id=1)

        SubMenu.objects.create(
            title="Fa",
            url="https://blog.test.org/fa",
            parent=menu_item,
            order="1",
        )