from django.urls import path
from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.main, name='main'),
    path('patient_info/', views.patient_info, name='patient_info'),
]