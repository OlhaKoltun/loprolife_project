from django.urls import path
from . import views

app_name = 'app_users'
urlpatterns = [
    path('', views.main, name='main'),
    path('user_info/', views.user_info, name='user_info'),
]