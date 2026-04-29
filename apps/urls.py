from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('unpublished/post/', views.Home.as_view(), name='unpublished'),
    path('create-post/', views.CreatePost.as_view(), name='create-post'),
    path('update/post/<int:id>/', views.UpdatePost.as_view(), name='update-post'),
]