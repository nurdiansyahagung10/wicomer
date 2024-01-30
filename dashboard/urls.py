from django.urls import path
from .views import dashboard_store
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("store/", dashboard_store, name="dashboardstore")
]
