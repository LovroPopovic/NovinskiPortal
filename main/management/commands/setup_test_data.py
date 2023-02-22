import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *

NUM_PORTAL = 5
NUM_AUTHOR = 10
NUM_ARTICLE = 15

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [NewsPortal, Author,Article]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        for _ in range(NUM_PORTAL):
            portal = NewsPortalFactory()

        for _ in range(NUM_AUTHOR):
            author = AuthorFactory()

        for _ in range(NUM_ARTICLE):
            article = ArticleFactory()
        