from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('image/', views.image_emotion, name='image_emotion'),
    path('text/', views.text_emotion, name='text_emotion'),
]