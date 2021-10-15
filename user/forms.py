from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(required=False,
                             label='Введите почту',
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Ваш Email'
                             }))
    first_name = forms.CharField(required=True,
                                 label='* Введите Ваше имя',
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Имя'
                                 }))
    last_name = forms.CharField(required=True,
                                label='* Введите Вашу Фамилию',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Фамилия'
                                }))
    username = forms.CharField(required=True,
                               label='* Введите логин аккаунта',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'login'
                               }),
                               help_text='Без специальных знаков: " @ , . + - _ "',
                               error_messages={
                                   'unique': "Пользователь с таким логином уже существует.",
                               },
                               )
    password1 = forms.CharField(required=True,
                                label='* Придумайте пароль',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Пароль'
                                }))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False,
                             label='Изменить почту',
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Ваш Email'
                             }))
    first_name = forms.CharField(required=True,
                                 label='Изменить имя',
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Имя'
                                 }))
    last_name = forms.CharField(required=True,
                                label='Изменить фамилию',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Фамилия'
                                }))
    username = forms.CharField(required=True,
                               label='Изменить логин',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'login'
                               }),
                               help_text='Без специальных знаков: " @ , . + - _ "',
                               error_messages={
                                   'unique': "Пользователь с таким логином уже существует.",
                               },
                               )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(widget=forms.FileInput(attrs={'onchange': 'form.submit()'}))

    class Meta:
        model = Profile
        fields = ['img', 'sexy', 'agree']
