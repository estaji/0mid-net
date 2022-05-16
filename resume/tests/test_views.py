from django.test import TestCase
from django.urls import reverse
from datetime import date
from resume.models import (
    Job,
    Education,
    TechSkill,
    SoftSkill,
    Language,
    Jumbotron,
    Configuration,
    SocialAccount,
)


class ResumeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Configuration.objects.create(
            site_title='My site',
            title='My full name',
            description='This is my personal website',
            robots='follow',
            author='Mr Test',
            keywords='personal blog, tag',
            copyr='All rights reserved',
        )
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
        Education.objects.create(
            university='Stanford',
            level='PhD',
            title='Computer Security',
            description='protection of computer systems',
            start=date.today(),
            end=None,
        )
        TechSkill.objects.create(
            title='Network Administration',
            certs='CCIE',
            details='the highest networking certifications in the industry.',
            order=1,
        )
        SoftSkill.objects.create(
            title='Leadership',
            order=2,
        )
        Language.objects.create(
            title='English',
            level='IELTS 9',
            order=3,
        )
        Jumbotron.objects.create(
            greeting='Welcome to my site',
            title='My full name',
            description='This is my personal website',
            email='me@test.com',
        )
        SocialAccount.objects.create(
            linkedin='https://www.linkedin.com/in/acc',
            github='https://github.com/acc',
            stackexchange='https://stackexchange.com/users/acc',
            instagram='',
            twitter='https://twitter.com/acc',
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resume'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('resume'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/resume.html')
