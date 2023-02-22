from django.contrib import admin
from .models import NewsPortal, Author, Article

@admin.register(NewsPortal)
class NewsPortalAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
