from django.test import TestCase
from datetime import date
from resume.models import (
    Job,
    Education,
    TechSkill,
    TechSkillText,
    SoftSkill,
    Language,
    Jumbotron,
    ResumeConfig,
    SocialAccount,
)


class JobModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Job.objects.create(
            title='Software Engineer',
            company='Google',
            url='https://google.com',
            company_details='An enterprise company',
            start=date.today(),
            end=None,
            location='USA',
            summary='Lead all tech departments',
        )
        Job.objects.create(
            start=date.today(),
            end=date.today()
        )

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

        self.assertEqual(end_field, 'Present')

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

        self.assertEqual(item.title, 'Software Engineer')
        self.assertEqual(item.company, 'Google')
        self.assertURLEqual(item.url, 'https://google.com')
        self.assertEqual(item.company_details, 'An enterprise company')
        self.assertEqual(item.location, 'USA')
        self.assertEqual(item.summary, 'Lead all tech departments')


class EducationModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Education.objects.create(
            university='Stanford',
            level='PhD',
            title='Computer Security',
            description='protection of computer systems',
            start=date.today(),
            end=None,
        )
        Education.objects.create(
            start=date.today(),
            end=date.today()
        )

    def test_add_education(self):
        """Test add a education"""
        item = Education.objects.get(id=1)

        self.assertEqual(item.title, 'Computer Security')
        self.assertEqual(item.university, 'Stanford')
        self.assertEqual(item.level, 'PhD')
        self.assertEqual(item.description, 'protection of computer systems')

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

        self.assertEqual(end_field, 'Present')

    def test_modified_end_year(self):
        """Test education end field returns modified date when is NOT empty"""
        item = Education.objects.get(id=2)
        date1 = Education.modified_end(item)
        for_date2 = item.end
        date2 = for_date2.strftime("%Y")

        self.assertEqual(date1, date2)


class TechSkillModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        TechSkill.objects.create(
            title='Network Administration',
            certs='CCIE',
            details='the highest networking certifications in the industry.',
            order=1,
        )

    def test_add_techskill(self):
        """Test add a technical skill in accordion style"""
        item = TechSkill.objects.get(id=1)

        self.assertEqual(item.title, 'Network Administration')
        self.assertEqual(item.certs, 'CCIE')
        self.assertEqual(
            item.details,
            'the highest networking certifications in the industry.'
        )
        self.assertEqual(item.order, 1)


class TechSkillTextModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        TechSkillText.objects.create(
            content='A Simple Content',
        )

    def test_add_techskilltext(self):
        """Test add a technical skill in text style"""
        item = TechSkillText.objects.get(id=1)

        self.assertEqual(item.content, 'A Simple Content')


class SoftSkillModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        SoftSkill.objects.create(
            title='Leadership',
            order=2,
        )

    def test_add_softskill(self):
        """Test add a soft skill"""
        item = SoftSkill.objects.get(id=1)

        self.assertEqual(item.title, 'Leadership')
        self.assertEqual(item.order, 2)


class LanguageModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Language.objects.create(
            title='English',
            level='IELTS 9',
            order=3,
        )

    def test_add_language(self):
        """Test add a language"""
        item = Language.objects.get(id=1)

        self.assertEqual(item.title, 'English')
        self.assertEqual(item.level, 'IELTS 9')
        self.assertEqual(item.order, 3)


class JumbotronModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Jumbotron.objects.create(
            greeting='Welcome to my site',
            title='My full name',
            occupation='An Engineer',
            description='This is my personal website',
            email='me@test.com',
        )

    def test_add_jumbotron(self):
        """Test add a jumbotron"""
        item = Jumbotron.objects.get(id=1)

        self.assertEqual(item.greeting, 'Welcome to my site')
        self.assertEqual(item.title, 'My full name')
        self.assertEqual(item.occupation, 'An Engineer')
        self.assertEqual(item.description, 'This is my personal website')
        self.assertEqual(item.email, 'me@test.com')


class SocialAccountModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        SocialAccount.objects.create(
            linkedin='https://www.linkedin.com/in/acc',
            github='https://github.com/acc',
            stackexchange='https://stackexchange.com/users/acc',
            instagram='',
            twitter='https://twitter.com/acc',
        )

        def test_add_socialaccount(self):
            """Test add a social account object"""
            item = SocialAccount.objects.get(id=1)

            self.assertURLEqual(
                item.linkedin,
                'https://www.linkedin.com/in/acc',
            )
            self.assertURLEqual(item.github, 'https://github.com/acc')
            self.assertURLEqual(
                item.stackexchange,
                'https://stackexchange.com/users/acc',
            )
            self.assertURLEqual(item.instagram, '')
            self.assertURLEqual(item.twitter, 'https://twitter.com/acc')


class ResumeConfigModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        ResumeConfig.objects.create(
            site_title='My site',
            title='My full name',
            description='This is my personal website',
            robots='follow',
            author='Mr Test',
            keywords='personal blog, tag',
            og_title='My OpenGraph title',
            twitter_user='username',
            skills_style="t"
        )

    def test_add_configuration(self):
        """Test add a configuration"""
        item = ResumeConfig.objects.get(id=1)

        self.assertEqual(item.site_title, 'My site')
        self.assertEqual(item.title, 'My full name')
        self.assertEqual(item.description, 'This is my personal website')
        self.assertEqual(item.robots, 'follow')
        self.assertEqual(item.author, 'Mr Test')
        self.assertEqual(item.keywords, 'personal blog, tag')
        self.assertEqual(item.og_title, 'My OpenGraph title')
        self.assertEqual(item.twitter_user, 'username')
        self.assertEqual(item.skills_style, 't')
