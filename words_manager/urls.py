from django.urls import path
from . import views


app_name = 'words_manager'
urlpatterns = [
    path('sets_display/', views.sets_display, name='sets_display'),
    path('set_add', views.set_add, name='set_add'),
]