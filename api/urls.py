from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('user_game/', views.UserGameAPI.as_view()),
    path('game/', views.GroupSessionAPI.as_view()),
    path('student/', views.StudentSessionAPI.as_view()),
    path('start_game/', views.StartGameSessionAPI.as_view()),

    path('auth/', include("djoser.urls")),
    re_path(r'^auth/', include("djoser.urls.authtoken")),
]
