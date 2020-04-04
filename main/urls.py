from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    #path('', views.user_panel, name='user_panel')
    path('', views.learn, name='learn')
]