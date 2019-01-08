from django.urls import path
from . import views

app_name= 'mainboard'

urlpatterns = [
    path('',views.get_all_moth,name = 'all_mainboards'),
    path('mainboard/<slug:slug>/', views.get_moth_detail, name='mainboard_detail'),
    
]