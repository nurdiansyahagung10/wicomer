from django.shortcuts import redirect
from functools import wraps

def user_is_authenticated(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return func(request, *args, **kwargs)
    return wrapper
