from django.urls import path
from . import views
app_name = 'graphic'

urlpatterns = [
    path('', views.get_all_graphic, name = 'all_graphic'),
    path('<slug:slug>/', views.get_graphic_detail, name='graphic_detail')
]
