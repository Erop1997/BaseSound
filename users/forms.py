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
<<<<<<< HEAD
   password1 = forms.CharField(widget=forms.PasswordInput(), label='Придумайте пароль')          
   password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')
   email = forms.EmailField(label='Введите адресс эл.почты')
=======
   password1 = forms.CharField(widget=forms.PasswordInput, label='Придумайте пароль')          
   password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')
   email = forms.EmailField('Введите адресс эл.почты')
>>>>>>> b86369d7d518cab58d85c462a8cf8ccdd3e30ec5

   class Meta:
       model = User
       fields = ['username', 'password1', 'password2', 'email']  
<<<<<<< HEAD

class ResetPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(), label='Текущий пароль')
    new_password1 = forms.CharField(widget=forms.PasswordInput(), label='Новый пароль')
    new_password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите новый пароль')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2'] 
=======
>>>>>>> b86369d7d518cab58d85c462a8cf8ccdd3e30ec5
