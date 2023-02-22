import factory
from .models import NewsPortal, Author, Article

class NewsPortalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NewsPortal

    name = factory.Faker('company')
    url = factory.Faker('url')

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')
    bio = factory.Faker('text')
    news_portal = factory.SubFactory(NewsPortalFactory)

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence')
    content = factory.Faker('text')
    news_portal = factory.SubFactory(NewsPortalFactory)