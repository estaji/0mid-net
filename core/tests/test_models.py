from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Menu, CoreConfig


class UserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@0mid.net'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@0MID.net'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@0mid.net',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


class MenuModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(
            title='Blog',
            url='https://blog.test.org',
            order='2',
            icon_type='N',
        )

    def test_add_menu_item(self):
        """Test add an item to menu"""
        item = Menu.objects.get(id=1)

        self.assertEqual(item.url, 'https://blog.test.org')


class CoreConfigModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        CoreConfig.objects.create(
            google_analytics='UA-155242907-7',
            copyr='All rights reserved',
        )

    def test_add_configuration(self):
        """Test add a configuration"""
        item = CoreConfig.objects.get(id=1)

        self.assertEqual(item.google_analytics, 'UA-155242907-7')
        self.assertEqual(item.copyr, 'All rights reserved')
