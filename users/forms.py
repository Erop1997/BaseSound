from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Введите никнейм')
    password = forms.CharField(widget=forms.PasswordInput() ,label='Введите пароль')

    class Meta:
        model = User
        fields = ['username', 'password']

class SignUpForm(UserCreationForm):
   username = forms.CharField(label='Придумайте никнейм')
   password1 = forms.CharField(widget=forms.PasswordInput, label='Придумайте пароль')          
   password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')
   email = forms.EmailField('Введите адресс эл.почты')

   class Meta:
       model = User
       fields = ['username', 'password1', 'password2', 'email']  
