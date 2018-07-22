from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Mainboard_info
from .form import *

# Create your views here.


def get_all_moth(request): # this the homepage
    all_moths = Mainboard_info.objects.all()
    contexts = {
        'all_moths':all_moths
    }

    return render(request,'motherboard/all_moth.html',context=contexts)

def get_moth_detail(request,slug):
    mainboard_inst = get_object_or_404(Mainboard_info,slug=slug)
    context = {
        "mainboard": mainboard_inst
    }
    return render(request, 'motherboard/moth_detail.html',context=context)
    
def handle_form(request):
    mainboard_form = MainboardForm()
    market_form = MainboardMarketForm()['market']
    # img_form = MainboardImgForm()
    # print(market_form['market'])
    if request.method == 'POST':
        print(request.POST)
        post_data = request.POST.copy()
        market = post_data.pop('market_name')
        price = post_data.pop('price')
        return_form = MainboardForm(post_data)
        print(request.FILES)
        if(return_form.is_valid()):
            pass
            # return redirect('/')  
    context = {
        'info_form':mainboard_form,
        'market_form':market_form
    }

    return render(request,'forms/moth.html',context)