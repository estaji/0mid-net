from django.test import TestCase
from django.urls import reverse


class BlogListViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        """Test view url exists at desired location for /blog/ """
        response = self.client.get('/blog/')

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test view url accessible by blog:home"""
        response = self.client.get(reverse('blog:home'))

        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """test view uses correct template for blog:home"""
        response = self.client.get(reverse('blog:home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
