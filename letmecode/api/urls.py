from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path("login/", obtain_auth_token),
    path("register/", views.Register.as_view()),
    path("test-is-auth/", views.TestIsAuth.as_view()),
    path("user/<str:username>/", views.GetUser.as_view()),
    path("project/<int:project_id>/", views.GetProject.as_view()),
    path("file/<int:file_id>/", views.GetFile.as_view()),
]
