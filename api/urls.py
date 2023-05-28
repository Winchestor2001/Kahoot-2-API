from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('user_game/', views.UserGameAPI.as_view()),

    path('auth/', include("djoser.urls")),
    re_path(r'^auth/', include("djoser.urls.authtoken")),
]
