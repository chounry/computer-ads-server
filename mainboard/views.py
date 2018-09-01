from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.forms import formset_factory

from .models import Mainboard_info
from .models import Image, Mainboard_market
from .form import *

# Create your views here.


def get_all_moth(request): # this the homepage
    all_moths = Mainboard_info.objects.all()
    contexts = {
        'all_moths':all_moths
    }

    return render(request,'motherboard/moth_pro_list.html',context=contexts)

def get_moth_detail(request,slug):
    mainboard_inst = get_object_or_404(Mainboard_info,slug=slug)
    context = {
        "mainboard": mainboard_inst
    }
    return render(request, 'motherboard/moth_detail.html',context=context)
    
def handle_form(request):
    mainboard_form = MainboardForm()
    market_form = MainboardMarketForm()['market']    

    if request.method == 'POST':
        post_data = request.POST.copy()

        market = {
            'market' : post_data.pop('market'),
            'prize' : post_data.pop('prize'),
            'link' : post_data.pop('link')
        }
        

        market_valid = True
        img_valid = True # give a default to true to prevent mainboard from check valid
        
        # if( market and prize and link):
        #     market_ret_form = MainboardMarketForm(request.POST)
        #     market_valid = market_ret_form.is_valid()
    
        if request.FILES:
            img_ret_form = MainboardImgForm(request.POST, request.FILES)
            img_valid = img_ret_form.is_valid()
        print(market_valid)

        info_ret_form = MainboardForm(request.POST)

        if info_ret_form.is_valid() and market_valid and img_valid:
            mainboard_instance = info_ret_form.save(commit=False)
            
            



    context = {
        'info_form':mainboard_form,
        'market_form':market_form
    }

    return render(request,'forms/moth.html',context)