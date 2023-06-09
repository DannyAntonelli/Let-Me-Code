from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from .views import user, project, file


urlpatterns = [
    path("user/login/", obtain_auth_token),
    path("user/register/", user.Register.as_view()),
    path("user/edit/", user.EditProfile.as_view()),
    path("user/search/", user.SearchUsers.as_view()),
    path("user/following/", user.GetFollowingUsers.as_view()),
    path("user/<str:username>/", user.GetUser.as_view()),
    path("user/<str:username>/follow/", user.FollowUser.as_view()),
    path("project/<int:project_id>/", project.GetProject.as_view()),
    path("project/create_project/", project.CreateProject.as_view()),
    path(
        "project/<int:project_id>/share/",
        project.ShareProject.as_view(),
    ),
    path(
        "project/<int:project_id>/public/",
        project.MakePublic.as_view(),
    ),
    path(
        "project/<int:project_id>/favorite/",
        project.ToggleFavorite.as_view(),
    ),
    path(
        "project/<int:project_id>/create_file/",
        file.CreateFile.as_view(),
    ),
    path("project/search/", project.SearchProjects.as_view()),
    path("project/following/", project.GetFollowingProjects.as_view()),
    path("project/favorites/", project.GetFavoriteProjects.as_view()),
    path("project/<int:project_id>/delete/", project.DeleteProject.as_view()),
    path("file/<int:file_id>/", file.GetFile.as_view()),
    path("file/<int:file_id>/sync/", file.SyncFile.as_view()),
    path("file/<int:file_id>/delete/", file.DeleteFile.as_view()),
]
