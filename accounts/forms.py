from django.contrib.auth.forms import UserCreationForm, UserChangeForm,SetPasswordForm,PasswordResetForm
from .models import User
from django import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import check_password

class CustomInitialForgotAccountsForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"type": "hidden", "class": "z-n1", "id": "id_email" }), required=True, max_length=100)
    def clean(self):
        data = self.cleaned_data["email"]
        if '@' in data:
            self = data
        else:
            self.add_error('email', "Dangerous action detected")         

class ForgotAccountForms(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control   border ", "aria-describedby": "emailHelp"}), required=True, max_length=100)

    def clean(self):
        data = self.cleaned_data["email"]
        User = get_user_model()
        try:
            self = User.objects.get(email = data)
        except User.DoesNotExist:
            self.add_error('email', "No account connected to the email you entered")

 
class CustomPasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control border'}))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control border'}))

    def clean_new_password1(self):
        auth = authenticate( username = self.user.username)
        new_password1 = self.cleaned_data.get('new_password1')
        cek_pw = check_password(new_password1, auth.password)
        if cek_pw:
            raise forms.ValidationError("The new password cannot be the same as the old password")
        return new_password1


class UserForm (forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control   border ", "aria-describedby": "emailHelp"}), required=True, max_length=100)
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control   border '}))
    rememberme = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'exampleCheck1'}))
    def clean(self):
        ussername = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        auth = authenticate(username = ussername)
        if auth is not None:
                cek_pw = check_password(password, auth.password)
                if cek_pw is not True:
                    self.add_error('password', "password is incorret.")
        else:
            self.add_error('username', "username or email is incorret")
 

class UserChangeForm(UserChangeForm):
    first_name = None
    last_name = None
    class Meta:
        model = User
        fields = ('username', 'email')


class UserCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}), required=True, max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control border"}), required=True, max_length=100)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control border'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control border'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control border', 'type' : 'date'}))
    pelajar = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'exampleCheck1'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'pelajar',)

class AdminUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'pelajar',)
