from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.forms import modelformset_factory

from .models import Mainboard_info
from .models import Image, Mainboard_market
from .form import *

# Create your views here.

def get_all_moth(request): # homepage
    all_moths = Mainboard_info.objects.all()
    contexts = {
        'all_moths':all_moths
    }

    return render(request,'motherboard/moth_pro_list.html',context=contexts)

def get_moth_detail(request,slug):
    mainboard_inst = get_object_or_404(Mainboard_info,slug=slug)
    context = {
        "mainboard" : mainboard_inst
    }
    return render(request, 'motherboard/moth_detail.html',context=context)
    
def handle_form(request):
    mainboard_form = MainboardForm()
    market_form = MainboardMarketForm()['market']    

    if request.method == 'POST':
        market = {
            'market_id' : request.POST.getlist('market'),
            'prize' : request.POST.getlist('prize'),
            'link' : request.POST.getlist('link')
        }

        market_valid = True 
        m_formset = None # => In case there is no market form

        if( market['market_id'] and market['prize'] and market['link']):
            data = {
                'form-TOTAL_FORMS' : str(len(market['prize'])),
                'form-INITIAL_FORMS' : '0',
                'form-MAX_NUM_FORMS' : '',
                }

            z_market = zip(market['market_id'],market['prize'], market['link'])
            for index,val in enumerate(z_market):
                tmp = {
                    "form-%d-link"%index : val[2],
                    "form-%d-prize"%index : val[1],
                    "form-%d-market"%index : val[0]
                }
                data.update(tmp)

            MarketFormset = modelformset_factory(Mainboard_market,form=MainboardMarketForm)
            m_formset = MarketFormset(data)
            market_valid = m_formset.is_valid()

        info_ret_form = MainboardForm(request.POST)
        print(m_formset.errors)
        print(market_valid)
        if info_ret_form.is_valid() and market_valid:
            mainboard_instance = info_ret_form.save()
            
            # if the market formset availble 
            if m_formset:
                for form in m_formset:
                    market_instance = Mainboard_market(
                        link  = form.cleaned_data['link'],
                        prize = form.cleaned_data['prize'],
                        mainboard = mainboard_instance,
                        market = form.cleaned_data['market']
                    )
                    market_instance.save()

            if request.FILES:
                for f in request.FILES.getlist('image'):
                    img_instance = Image(image=f,mainboard=mainboard_instance)
                    img_instance.save()
        else:
            print('Not successful')
            # return the form with the previous data
            return render(request,'forms/moth_form.html',context = {'info_form' : info_ret_form,'market_form':market_form})

    context = {
        'info_form' : mainboard_form,
        'market_form' : market_form
    }

    return render(request,'forms/moth_form.html',context)