from django.test import TestCase
from datetime import date
from core.models import User
from blog.models import (
    Tag,
    Article
)


class TagModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            title='Django',
            slug='django-tag',
            position=1,
            meta_description='test meta description string',
            keywords='tagkw1, tagkw2'
        )
        User.objects.create(
            email='testuser@gmail.com',
            name='Linus Torvalds',
            is_active=True,
            is_staff=False
        )

    def test_add_tag(self):
        """Test add a tag to blog"""
        item = Tag.objects.get(id=1)

        self.assertEqual(item.title, 'Django')
        self.assertEqual(item.slug, 'django-tag')
        self.assertEqual(item.position, 1)
        self.assertEqual(item.meta_description, 'test meta description string')
        self.assertEqual(item.keywords, 'tagkw1, tagkw2')

    def test_posts_count(self):
        """Test posts count function can count articles for a tag"""
        self.article1 = Article.objects.create(
            author=User.objects.get(id=1),
            title='Test Article',
            slug='test-article',
            subheading='this is a test text',
            content='this is a test content',
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status='p',
            language='en'
        )

        self.article1.tag.add(Tag.objects.get(id=1))
        item = Tag.objects.get(id=1)
        number_of_posts = Tag.posts_count(item)

        self.assertEqual(number_of_posts, 1)

    def test_posts_count_only_published_articles(self):
        """Test posts count function only count published articles for a tag"""
        self.article1 = Article.objects.create(
            author=User.objects.get(id=1),
            title='Test Article',
            slug='test-article',
            subheading='this is a test text',
            content='this is a test content',
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status='p',
            language='en'
        )
        self.article2 = Article.objects.create(
            author=User.objects.get(id=1),
            title='Drafted Article',
            slug='draft-article',
            subheading='this is a test text',
            content='this is a test content',
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status='d',
            language='en'
        )

        self.article1.tag.add(Tag.objects.get(id=1))
        self.article2.tag.add(Tag.objects.get(id=1))
        item = Tag.objects.get(id=1)
        number_of_posts = Tag.posts_count(item)

        self.assertEqual(number_of_posts, 1)
