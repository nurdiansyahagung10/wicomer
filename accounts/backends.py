from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.http import Http404

class AuthenticateUsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username = None ,  **kwargs):
        User = get_user_model()
        if username is not None:
            try:
                if '@' in username:
                    user = User.objects.get(email_address = username)
                    return user
                else :
                    user = User.objects.get(username = username)
                    return user
            except User.DoesNotExist:
                return None
            except User.MultipleObjectsReturned:
                raise Http404
        else:
            return None        
                