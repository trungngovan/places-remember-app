from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("oauth2callback/", views.oauth2callback, name="oauth2callback"),
    path("logout/", views.logout_view, name="logout"),
    path("memory/add/", views.add_memory, name="add_memory"),
]
