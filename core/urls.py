
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core import settings
urlpatterns = [
    path("", home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
] 
