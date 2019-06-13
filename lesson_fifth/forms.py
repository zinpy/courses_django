from django.forms import ModelForm
from .models import Author, Article


class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'surname', 'city']


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        # fields = ['author', 'title', 'text']
        fields = '__all__'
