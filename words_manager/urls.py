from django.urls import path
from . import views


app_name = 'words_manager'
urlpatterns = [
    path('display_topics/', views.display_topics, name='display_topics')
    #path('add_topics/', views.add_topics, name='add_topics')
]