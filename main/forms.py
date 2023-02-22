from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'news_portal', 'authors']

class ArticleDeleteForm(forms.Form):
    article_id = forms.IntegerField(widget=forms.HiddenInput())
