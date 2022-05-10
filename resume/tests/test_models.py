from django.test import TestCase
from datetime import date
from resume.models import Job


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

    def test_add_education(self):
        """Test add a education"""
        pass

    def test_short_start_year(self):
        """Test education start date shows year"""
        pass

    def test_modified_end_year_present(self):
        """Test education end field returns PRESENT when is empty"""
        pass

    def test_modified_end_year(self):
        """Test education end field returns modified date when is NOT empty"""
        pass
