from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .forms import UserForm, UserCreateForm, ForgotAccountForms,CustomInitialForgotAccountsForm,CustomPasswordChangeForm, StoreForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, get_user_model,logout
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_authenticated
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse_lazy
from .models import Store

def createstore(request):
    try:
        Store.objects.get(store_seller_id = request.user)
        return redirect('dashboardstore')
    except Store.DoesNotExist:
        form = StoreForm()    
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store_image = form.cleaned_data.get('store_image')
            phonenumber = form.cleaned_data.get('phonenumber')
            email = form.cleaned_data.get('email')
            store_name = form.cleaned_data.get('store_name')
            store_description = form.cleaned_data.get('store_description')
            store_open = form.cleaned_data.get('store_open')
            store_closed = form.cleaned_data.get('store_closed')
            store = Store(
                store_seller_id = request.user,
                store_image = store_image,
                phonenumber = phonenumber,
                email = email,
                store_name = store_name,
                store_description = store_description,
                store_open = store_open,
                store_closed = store_closed,
            )            
            store.save()
            return redirect('dashboardstore')
    return render(request, 'accounts/create_store.html', {'form':form})
        

    
@login_required
def logoutview (request):
    logout(request)
    return redirect('signin')

class CustomInitialResetPassword(PasswordResetView):
    template_name = 'accounts/initiate_accounts_forgot.html'
    form_class = CustomInitialForgotAccountsForm       
    success_url = reverse_lazy("signin")

    def dispatch(self, request, *args, **kwargs):
        self.email = kwargs.get('email')
        email_decode = urlsafe_base64_decode(self.email)
        User = get_user_model()
        try:
            user = User.objects.get(email=email_decode.decode())
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
        ):
            raise Http404()
        self.user = user
        return super().dispatch(request, *args, **kwargs)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = self.user  
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Instructions to reset your password will be sent to you. Please check your email.')
        return super().form_valid(form)


def ForgotAccountsViews(request):
    form = ForgotAccountForms()
    if request.method == 'POST':
        form = ForgotAccountForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if email is not None:
                uid = urlsafe_base64_encode(str(email).encode('utf-8'))
                return redirect('forgot_accounts_initiate', email = uid)
                
    return render(request, 'accounts/forgot_accounts_or_password.html', {'form' : form})


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('signin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Change Password'  
        return context
    def form_valid(self, form):
        messages.success(self.request, 'Password successfully updated.')
        return super().form_valid(form)
    
def SignUpView(request):
    form = UserCreateForm() 
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            password = form.cleaned_data.get('password1')
            User = get_user_model()
            user = User(username = username, email = email, date_of_birth =date_of_birth)
            user.set_password(password)
            user.save()
            return redirect ('signin')
    return render(request, 'accounts/signup.html', {'form' : form, })        

@user_is_authenticated
def SignInView(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password') 
            remember_me = form.cleaned_data.get('rememberme')
            user = authenticate(request, username = username, password = password)
            if not remember_me:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(2592000)
            login(request, user)
            return redirect('home')
    return render (request, 'accounts/signin.html', {'form' : form})

