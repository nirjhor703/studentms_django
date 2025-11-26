from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('watch/<str:file_id>/', views.watch_video, name='watch_video'),
    path('download/<str:file_id>/', views.download_video, name='download_video'),
]
