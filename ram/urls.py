from django.urls import path
from . import views

app_name = 'ram'

urlpatterns = [
    path('',views.get_all_ram, name='all_ram'),
    path('<slug:slug>/',views.get_ram_detail, name='ram_detail')
]