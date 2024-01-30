from django.urls import path,include
from .views import SignInView,SignUpView,logoutview,ForgotAccountsViews,CustomInitialResetPassword,CustomPasswordResetConfirmView,createstore
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('google/', include('social_django.urls', namespace='social')),
    path('forgot-accounts-or-password/', ForgotAccountsViews, name='forgot_accounts_or_password'),
    path('forgot-accounts-or-password/initiate/<email>', CustomInitialResetPassword.as_view(), name='forgot_accounts_initiate'),
    path('forgot-accounts-or-password/<uidb64>/<token>/change-password/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("store_create/", createstore, name="storecreate"),
    path("sign-in/", SignInView, name="signin"),
    path("sign-up/", SignUpView, name="signup"),
    path("sign-out/", logoutview, name="signout")
]
