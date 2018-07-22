from django.shortcuts import render, get_object_or_404

from .models import *

# Create your views here.
def get_all_ram(request):
    all_ram = Memory_info.objects.all()
    context = {
        'all_ram': all_ram
    }
    return render(request, 'ram/all_ram.html', context=context)

def get_ram_detail(request, slug):
    ram = get_object_or_404(Memory_info, slug=slug)
    context = {
        'ram': ram
    }
    return render(request, 'ram/ram_detail.html', context=context)