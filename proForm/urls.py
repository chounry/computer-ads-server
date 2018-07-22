from django.urls import path
from . import views
app_name = 'form'

urlpatterns = [
    path('mainboard/',views.mainboard_f, name='mainboard_form'),
    path('graphic-card/',views.mainboard_f, name='graphic_form'),
    path('ram/',views.mainboard_f, name='ram_form'),
    path('cpu/',views.mainboard_f, name='cpu_form'),
    
]