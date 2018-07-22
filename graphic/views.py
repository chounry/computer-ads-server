from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def get_all_graphic(request):
    all_graphic = Graphic_info.objects.all()
    context = {
        'all_graphic': all_graphic
    }
    return render(request, 'graphic/all_graphic.html', context)

def get_graphic_detail(request, slug):
    graphic = get_object_or_404(Graphic_info,slug=slug)
    context = {
        'graphic': graphic,
        'all_api': graphic.api_supp.all()
    }
    return render(request, 'graphic/graphic_detail.html', context=context)
