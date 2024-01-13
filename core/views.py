from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import get_user_model

def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('signin')