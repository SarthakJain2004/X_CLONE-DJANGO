# core/urls.py
from django.urls import path, include
from . import views, api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", api_views.PostViewSet, basename="post")

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_post, name="create_post"),
    path("like/<int:pk>/", views.like_post, name="like_post"),
    path("comment/<int:pk>/", views.add_comment, name="comment"),
    path("edit/<int:pk>/", views.edit_post, name="edit_post"),      
    path("delete/<int:pk>/", views.delete_post, name="delete_post"), 
    path("signup/", views.signup, name="signup"),
    path("api/", include(router.urls)),
]
