from django import forms
from django.forms import ModelForm
from .models import Author, Article
from django.core.validators import URLValidator, ValidationError


class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'surname', 'city']


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        # fields = ['author', 'title', 'text']
        fields = '__all__'


class ContactForm(forms.Form):
    boolean_field = forms.BooleanField(required=False)
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label="Введите ваше имя")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")
    sender = forms.EmailField(label="Введите ваш емейл!")


def validate_url(url):
    validation_url = URLValidator()
    invalid = 0

    try:
        validation_url(url)
    except:
        invalid += 1

    url1 = 'http://' + url

    try:
        validation_url(url1)
    except:
        invalid += 1

    if invalid != 1:
        raise ValidationError('Это не адрес сайта!')

    return url


class UrlForm(forms.Form):
    title = forms.CharField(label='Название сайта')
    url = forms.CharField(label='Адрес сайта', validators=[validate_url])

    # def clean(self):
    #     cleaned_data = super(UrlForm, self).clean()

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     validation_url = URLValidator(message='Это не адрес сайта!')
    #     validation_url(url)
    #     # try:
    #     #     validation_url(url)
    #     # except:
    #     #     raise forms.ValidationError('Это не адрес сайта!')
    #     return url

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     validation_url = URLValidator()
    #     invalid = 0
    #
    #     try:
    #         validation_url(url)
    #     except:
    #         invalid += 1
    #
    #     url1 = 'http://' + url
    #
    #     try:
    #         validation_url(url1)
    #     except:
    #         invalid += 1
    #
    #     if invalid != 1:
    #         raise forms.ValidationError('Это не адрес сайта!')
    #
    #     return url
