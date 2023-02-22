from django.urls import path
from main.views import *
from django.contrib.auth import views as auth_views
from main.auth_views import login_view, register_view, logout_view


urlpatterns = [
    path('', login_view, name='login'),
    path('base/', base, name='base'),
    path('newsportal/', NewsPortalList.as_view(), name='newsportal_list'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('article/', ArticleList.as_view(), name='article_list'),
    path('article/create/', create_article, name='create_article'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
   
]