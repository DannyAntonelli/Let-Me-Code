from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path("login/", obtain_auth_token),
    path("register/", views.Register.as_view()),
    path("test-is-auth/", views.TestIsAuth.as_view()),
]
