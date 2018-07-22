from django.urls import path
from . import views

app_name = "cpu"

urlpatterns = [
    path("", views.get_all_cpu, name="all_cpu"),
    path("<slug:slug>/", views.get_cpu_detail, name="cpu_detail")
]