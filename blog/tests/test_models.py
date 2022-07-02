from django.test import TestCase
from datetime import date
from core.models import User
from blog.models import (
    Tag,
    Article,
    Configuration
)


class TagAndArticleModelTests(TestCase):

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

    def test_add_article(self):
        """Test add an article"""
        self.article1 = Article.objects.create(
            author=User.objects.get(id=1),
            title='test title',
            slug='test-slug',
            subheading='this is a text',
            content='this is a test content',
            published=date.today(),
            created=date.today(),
            updated=date.today(),
            status='p',
            language='en',
            meta_description='vim is a test meta',
            keywords='testkw1, kw2',
            robots='follow',
        )
        self.article1.tag.add(Tag.objects.get(id=1))

        item = Article.objects.get(id=1)

        self.assertEqual(item.author, User.objects.get(id=1))
        self.assertEqual(item.title, 'test title')
        self.assertEqual(item.slug, 'test-slug')
        self.assertEqual(item.subheading, 'this is a text')
        self.assertEqual(item.content, 'this is a test content')
        self.assertEqual(item.published, date.today())
        self.assertEqual(item.created, date.today())
        self.assertEqual(item.updated, date.today())
        self.assertEqual(item.status, 'p')
        self.assertEqual(item.language, 'en')
        self.assertEqual(item.meta_description, 'vim is a test meta')
        self.assertEqual(item.keywords, 'testkw1, kw2')
        self.assertEqual(item.robots, 'follow')
        self.assertTrue(item.tag.exists())


class ConfigurationModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Configuration.objects.create(
            copyr='all rights for me',
            email='testemail@hotmail.com',
            linkedin='https://linkedin.com/in/test-user/',
            name='My blog',
            title='My blog title',
            subtitle='this is my blog',
            meta_author='written by test user',
            meta_description='this is all about my road',
            keywords='keyword1, keyword2',
            robots='index',
        )

    def test_add_configuration(self):
        """Test add a configuration"""
        item = Configuration.objects.get(id=1)

        self.assertEqual(item.copyr, 'all rights for me')
        self.assertEqual(item.email, 'testemail@hotmail.com')
        self.assertEqual(item.linkedin, 'https://linkedin.com/in/test-user/')
        self.assertEqual(item.name, 'My blog')
        self.assertEqual(item.title, 'My blog title')
        self.assertEqual(item.subtitle, 'this is my blog')
        self.assertEqual(item.meta_author, 'written by test user')
        self.assertEqual(item.meta_description, 'this is all about my road')
        self.assertEqual(item.keywords, 'keyword1, keyword2')
        self.assertEqual(item.robots, 'index')
