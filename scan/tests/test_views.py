from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from datetime import datetime
from core.models import User
from scan.models import Node, Job


class HomeViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Node.objects.create(
            node_type='p',
            location='IR-Parseh',
            url='www.srv.mysite.com',
            is_active=True,
        )

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location"""
        response = self.client.get('/scan/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by app:urlname"""
        response = self.client.get(reverse('scan:scan-home'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template"""
        response = self.client.get(reverse('scan:scan-home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scan/home.html')

    def test_valid_url_post_request(self):
        """Test a valid post request will redirects for home scan page"""
        response = self.client.post(
            '/scan/',
            {'url': 'www.google.com', 'action': 'ping'}
        )

        self.assertEqual(response.status_code, 302)

    def test_valid_http_action_post_request(self):
        """Test a valid http action post request,"""
        """will redirects for home scan page"""

        response = self.client.post(
            '/scan/',
            {'url': 'www.google.com', 'action': 'http'}
        )

        self.assertEqual(response.status_code, 302)

    def test_invalid_url_post_request(self):
        """Test an invalid post request will show a error"""
        bad_url = 'wwwgoogle'
        response = self.client.post('/scan/', data={'url': bad_url})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter a valid URL')

    def test_invalid_action_post_request(self):
        """Test an invalid action post request will show a error"""
        response = self.client.post(
            '/scan/',
            {'url': 'www.google.com', 'action': 'invalidX'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid action')

    def test_empty_post_request(self):
        """Test an empty post request will show a error"""
        empty = ''
        response = self.client.post('/scan/', data={'url': empty})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required')


class ResultViewTest(TestCase):

    a_uuid = '07379a5f-7dfe-4efa-a8c5-038dbffd7da0'

    @classmethod
    def setUpTestData(cls):
        Node.objects.create(
            node_type='p',
            location='IR-Parseh',
            url='www.srv.mysite.com',
            is_active=True,
        )
        Job.objects.create(
            start_time=datetime.now(),
            command='pi',
            node=Node.objects.filter(location='IR-Parseh').first(),
            uuid='07379a5f-7dfe-4efa-a8c5-038dbffd7da0',
            url='www.pixel.ir',
        )
        Job.objects.create(
            start_time=datetime.now(),
            command='p',
            node=Node.objects.filter(location='IR-Parseh').first(),
            status='s',
            uuid='07379a5f-7dfe-4efa-a8c5-038dbffd7da0',
            url='www.pixel.ir',
            result='Ping OK'
        )

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location"""
        response = self.client.get('/scan/result/{}'.format(self.a_uuid))

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by app:urlname"""
        response = self.client.get(
            reverse('scan:result', kwargs={'uuid': self.a_uuid})
        )

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template"""
        response = self.client.get(
            reverse('scan:result', kwargs={'uuid': self.a_uuid})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scan/result.html')

    def test_not_exist_uuid_result_returns_404(self):
        """Test view returns 404 for a not exist uuid result"""
        not_exist_uuid = '0aabbcc1-7ddd-4eee-abcd-03838383838a'
        response = self.client.get(
            reverse('scan:result', kwargs={'uuid': not_exist_uuid})
        )

        self.assertEqual(response.status_code, 404)

    def test_progress_is_a_percent(self):
        """Test progress returns as a number less than 100 like a percent"""
        response = self.client.get(
            reverse('scan:result', kwargs={'uuid': self.a_uuid})
        )

        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(response.context['progress'], 100)


class FreshResultViewTest(TestCase):

    finished_uuid = '08389a5f-8dfe-4efa-a8c5-038dbffd8da0'
    running_uuid = '08389a5f-eeee-4efa-a8c5-038dbffd8da0'

    @classmethod
    def setUpTestData(cls):
        Node.objects.create(
            node_type='p',
            location='IR-Parseh',
            url='www.srv.mysite.com',
            is_active=True,
        )
        Job.objects.create(
            start_time=datetime.now(),
            command='pi',
            node=Node.objects.filter(location='IR-Parseh').first(),
            uuid='08389a5f-eeee-4efa-a8c5-038dbffd8da0',
            url='www.parspack.com',
        )
        Job.objects.create(
            start_time=datetime.now(),
            command='p',
            node=Node.objects.filter(location='IR-Parseh').first(),
            status='r',
            uuid='08389a5f-eeee-4efa-a8c5-038dbffd8da0',
            url='www.parspack.com',
        )
        Job.objects.create(
            start_time=datetime.now(),
            command='pi',
            node=Node.objects.filter(location='IR-Parseh').first(),
            uuid='08389a5f-8dfe-4efa-a8c5-038dbffd8da0',
            url='www.pixel.ir',
        )
        Job.objects.create(
            start_time=datetime.now(),
            command='p',
            node=Node.objects.filter(location='IR-Parseh').first(),
            status='s',
            uuid='08389a5f-8dfe-4efa-a8c5-038dbffd8da0',
            url='www.pixel.ir',
            result='Ping OK'
        )

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location"""
        response = self.client.get(
            '/scan/result/{}/freshresult'.format(self.running_uuid)
        )

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by app:urlname"""
        response = self.client.get(
            reverse(
                'scan:scan-fresh-result',
                kwargs={'uuid': self.running_uuid}
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template"""
        response = self.client.get(
            reverse(
                'scan:scan-fresh-result',
                kwargs={'uuid': self.running_uuid}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scan/fresh_result.html')

    def test_view_returns_286_for_completed_job(self):
        """Test view returns 286 status code for a progress==100 scan"""
        response = self.client.get(
            reverse(
                'scan:scan-fresh-result',
                kwargs={'uuid': self.finished_uuid}
            )
        )

        self.assertEqual(response.status_code, 286)
        self.assertEqual(response.context['progress'], 100)

    def test_not_exist_uuid_result_returns_404(self):
        """Test view returns 404 for a not exist uuid result"""
        not_exist_uuid = '0aakkcc1-7ddd-4eee-kkkk-03838383838a'
        response = self.client.get(
            '/scan/result/{}/freshresult'.format(not_exist_uuid)
        )

        self.assertEqual(response.status_code, 404)


class PingViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        myuser = User.objects.create(
            email='testuser@gmail.com',
            name='Cloud User',
            is_active=True,
            is_staff=False
        )
        Token.objects.create(user=myuser)

    def test_apiview_works_with_authentication(self):
        """Test apiview for pinging works well with token authentication"""
        client = APIClient()
        user = User.objects.get(email='testuser@gmail.com')
        client.credentials(HTTP_AUTHORIZATION='Token ' + str(user.auth_token))
        response = client.get('/scan/api/ping/?url=google.com')

        self.assertEqual(response.status_code, 200)

    def test_apiview_needs_authentication(self):
        """Test apiview returns 401 error without authentication"""
        client = APIClient()
        response = client.get('/scan/api/ping/?url=google.com')

        self.assertEqual(response.status_code, 401)

    def test_apiview_needs_url_parameter(self):
        """Test apiview needs url parameter to work"""
        client = APIClient()
        user = User.objects.get(email='testuser@gmail.com')
        client.credentials(HTTP_AUTHORIZATION='Token ' + str(user.auth_token))
        response = client.get('/scan/api/ping/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Need a url')
