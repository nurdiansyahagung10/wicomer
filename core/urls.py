
from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf.urls.static import static

from core import settings
urlpatterns = [
    path("", index, name="home"),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
