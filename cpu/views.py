from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def get_all_cpu(request):
    all_cpu = CPU_info.objects.all()
    context = {"all_cpu": all_cpu}
    return render(request, "cpu/all_cpu.html", context)

def get_cpu_detail(request, slug):
    cpu = get_object_or_404(CPU_info, slug=slug)
    context = {
        "cpu": cpu
    }
    return render(request, 'cpu/cpu_detail.html', context)