from accounts.views import LoginView
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
]