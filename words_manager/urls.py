from django.urls import path
from . import views


app_name = 'words_manager'
urlpatterns = [
    path('', views.display_topics, name='display_topics'),
    path('add_topic/', views.add_topic, name='add_topic'),
]