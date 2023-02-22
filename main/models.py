from django.db import models

class NewsPortal(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    def __str__(self):
        return f"{self.name}"

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # One-to-one 
    news_portal = models.OneToOneField(NewsPortal, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # One-to-many 
    news_portal = models.ForeignKey(NewsPortal, on_delete=models.CASCADE)
    # Many-to-many 
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return f"{self.title}"
