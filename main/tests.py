from django.test import TestCase
from .models import NewsPortal, Author, Article

class NewsPortalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        NewsPortal.objects.create(name='CNN', url='http://www.cnn.com', description='CNN news portal')

    def test_name_label(self):
        news_portal = NewsPortal.objects.get(id=1)
        field_label = news_portal._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_url_label(self):
        news_portal = NewsPortal.objects.get(id=1)
        field_label = news_portal._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'url')

    def test_description_label(self):
        news_portal = NewsPortal.objects.get(id=1)
        field_label = news_portal._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_name_max_length(self):
        news_portal = NewsPortal.objects.get(id=1)
        max_length = news_portal._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_name(self):
        news_portal = NewsPortal.objects.get(id=1)
        expected_object_name = f'{news_portal.name}'
        self.assertEqual(expected_object_name, str(news_portal))

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        news_portal = NewsPortal.objects.create(name='CNN', url='http://www.cnn.com', description='CNN news portal')
        Author.objects.create(name='John Doe', bio='Author bio', news_portal=news_portal)

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_bio_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.name}'
        self.assertEqual(expected_object_name, str(author))


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        news_portal = NewsPortal.objects.create(name='CNN', url='http://www.cnn.com', description='CNN news portal')
        author = Author.objects.create(name='John Doe', bio='Author bio', news_portal=news_portal)
        Article.objects.create(title='Article title', content='Article content', news_portal=news_portal)

    def test_title_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_content_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_title_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)