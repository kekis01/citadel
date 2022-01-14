from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

from main.models import Comments, Category, Article


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=16, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                           'placeholder': "Логин"
                                                                                           }))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input',
                                                                          'placeholder': "Email"}))
    password1 = forms.CharField(label='Пароль', max_length=24,
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  'placeholder': "Пароль",
                                                                  }))
    password2 = forms.CharField(label='Повтор пароля', max_length=24,
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  'placeholder': "Повтор пароля",
                                                                  }))
    field_order = ['username', 'email', 'password1', 'password2']

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=16, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                           'placeholder': "Логин"
                                                                                           }))
    password = forms.CharField(label='Пароль', max_length=24, widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                                'placeholder': "Пароль",
                                                                                                }))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    text = forms.CharField(label="Комментарий",
                           widget=forms.Textarea(attrs={'class': 'comment_form',
                                                        'placeholder': "Напиши, что думаешь(макс. 1000 символов)",
                                                        'rows': 1,
                                                        'cols': 172,
                                                        'maxlength': 1000}))


class CommentFormDisabled(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    text = forms.CharField(label="Комментарий",
                           widget=forms.Textarea(attrs={'class': 'comment_form',
                                                        'placeholder': "Зарегистрируйтесь, чтобы написать комментарий",
                                                        'rows': 1,
                                                        'cols': 172,
                                                        'maxlength': 1000,
                                                        'disabled': 'disabled'}))


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'source', 'photo', 'is_published', 'cat']

    title = forms.CharField(label="Заголовок", max_length=255, widget=forms.Textarea(
        attrs={'rows': 1, 'cols': 172, 'class': 'title_input', 'placeholder': "Напишите название вашей статьи"}))
    content = forms.CharField(label="Текст",
                              widget=forms.Textarea(
                                  attrs={'rows': 10, 'cols': 172, 'class': 'title_input',
                                         'placeholder': "О чем расскажете?"}))
    source = forms.CharField(label="Источник", max_length=255,
                             widget=forms.Textarea(attrs={'rows': 1, 'cols': 172, 'class': 'title_input',
                                                          'placeholder': "Укажите источник"}))
    photo = forms.ImageField(label="Фото", )
    is_published = forms.BooleanField(label="Публикация")
    cat = forms.ModelChoiceField(label="Категория", queryset=Category.objects.all(), )
