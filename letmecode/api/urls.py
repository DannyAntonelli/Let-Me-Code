from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path("login/", obtain_auth_token),
    path("register/", views.Register.as_view()),
    path("user/<str:username>/", views.GetUser.as_view()),
    path("project/<int:project_id>/", views.GetProject.as_view()),
    path("file/<int:file_id>/", views.GetFile.as_view()),
    path("create_project/", views.CreateProject.as_view()),
    path("<int:project_id>/create_file/", views.CreateFile.as_view()),
    path("file/<int:file_id>/sync/", views.SyncFile.as_view()),
    path("project/<int:project_id>/share/", views.ShareProject.as_view()),
    path("project/<int:project_id>/public/", views.MakePublic.as_view()),
]
