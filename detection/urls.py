from django.urls import path
from . import views

urlpatterns = [
    path('', views.detection, name='detection'),
    path('start/', views.start_detection, name='start_detection'),
    path('stop/', views.stop_detection, name='stop_detection'),
    path('video_feed/', views.video_feed, name='video_feed'),
]