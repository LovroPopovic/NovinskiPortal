from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NewsPortal, Author, Article
from django.views.generic import ListView
from .forms import ArticleForm

class NewsPortalList(ListView):
    model = NewsPortal

class AuthorList(ListView):
    model = Author

class ArticleList(ListView):
    model = Article
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

        
@login_required
def base(request):
    if 'base_redirect' in request.GET:
        if request.user.is_authenticated:
            return redirect('base')
        else:
            return redirect('login')
    return render(request, "main/base.html")


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        if 'delete' in request.POST:
            article.delete()
            return redirect('article_list')
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
    else:
        form = ArticleForm(instance=article)

    return render(request, 'main/article_detail.html', {'article': article, 'form': form})




def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'main/create_article.html', {'form': form})


def search_articles(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = []
    return render(request, 'main/search_articles.html', {'query': query, 'articles': articles})

@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')


@login_required
def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'main/create_article.html', {'form': form})