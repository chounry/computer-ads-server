from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from itertools import chain
# from django.db.models import Q

from .models import Mainboard_info,Image, Mainboard_market,Form_factor,Socket_type, Company
from cpu.models import CPU_info
from ram.models import Memory_info
from graphic.models import Graphic_info
from .form import *

# Create your views here.

def get_all_moth(request): # homepage

    # <------------- handle filter
    form_factors_req = request.GET.getlist('form_factor')
    company_req = request.GET.getlist('company')
    socket_req = request.GET.getlist('socket')

    form_factors_query = Form_factor.objects.filter(name__in = form_factors_req)
    company_query = Company.objects.filter(name__in = company_req)
    socket_query = Socket_type.objects.filter(name__in = socket_req)

    #these variable will send back to the template for comparing to find which has been selected
    form_factor_compare = form_factors_query
    company_compare = company_query
    socket_compare = socket_query

    # the var for displaying all the filter value on the top
    all_filter_val = chain(form_factor_compare,company_compare,socket_compare)
    
    # if the individual filter value is null then we give that query an all object so that we can search correctly
    company_query = company_query if company_query.exists() else Company.objects.all()
    form_factors_query = form_factors_query if form_factors_query.exists() else Form_factor.objects.all()
    socket_query = socket_query if socket_query.exists() else Socket_type.objects.all()
    
    all_moths = Mainboard_info.objects.filter(
        company__in = company_query,
        form_factor__in = form_factors_query ,
        socket_type__in = socket_query
    )

    # end handle filter ---------------->
    
    form_factors = Form_factor.objects.all()
    companies = Company.objects.all()
    sockets = Socket_type.objects.all()

    paginator = Paginator(all_moths, 12) # Show 25 contacts per page

    page = request.GET.get('page')
    all_moths = paginator.get_page(page)
    contexts = {
        'form_factors': form_factors,
        'companies' : companies,
        'sockets': sockets,
        'all_moths':all_moths,

        'form_factor_compare':form_factor_compare,
        'company_compare':company_compare,
        'socket_compare':socket_compare,

        'all_filter_val':all_filter_val

    }

    return render(request,'motherboard/moth_pro_list.html',context=contexts)

def get_moth_detail(request,slug):
    mainboard_inst = get_object_or_404(Mainboard_info,slug=slug)

    supported_cpu = CPU_info.objects.filter(socket_type = mainboard_inst.socket_type)
    supported_ram = Memory_info.objects.filter(mem_tech = mainboard_inst.mem_tech)
    supported_gpu = Graphic_info.objects.filter(expansion_slot__in = mainboard_inst.expan_slot.all())


    print(len(supported_gpu),len(supported_ram),len(supported_cpu))
    context = {
        "mainboard" : mainboard_inst,
        "supp_cpu" : supported_cpu,
        "supp_ram" : supported_ram,
        "supp_gpu" : supported_gpu
    }
    return render(request, 'motherboard/moth_detail.html',context=context)






  
    
# def handle_form(request):
#     mainboard_form = MainboardForm()
#     market_form = MainboardMarketForm()['market']    

#     if request.method == 'POST':
#         market = {
#             'market_id' : request.POST.getlist('market'),
#             'prize' : request.POST.getlist('prize'),
#             'link' : request.POST.getlist('link')
#         }

#         market_valid = True 
#         m_formset = None # => In case there is no market form

#         if( market['market_id'] and market['prize'] and market['link']):
#             data = {
#                 'form-TOTAL_FORMS' : str(len(market['prize'])),
#                 'form-INITIAL_FORMS' : '0',
#                 'form-MAX_NUM_FORMS' : '',
#                 }

#             z_market = zip(market['market_id'],market['prize'], market['link'])
#             for index,val in enumerate(z_market):
#                 tmp = {
#                     "form-%d-link"%index : val[2],
#                     "form-%d-prize"%index : val[1],
#                     "form-%d-market"%index : val[0]
#                 }
#                 data.update(tmp)

#             MarketFormset = modelformset_factory(Mainboard_market,form=MainboardMarketForm)
#             m_formset = MarketFormset(data)
#             market_valid = m_formset.is_valid()

#         info_ret_form = MainboardForm(request.POST)
#         print(m_formset.errors)
#         print(market_valid)
#         if info_ret_form.is_valid() and market_valid:
#             mainboard_instance = info_ret_form.save()
            
#             # if the market formset availble 
#             if m_formset:
#                 for form in m_formset:
#                     market_instance = Mainboard_market(
#                         link  = form.cleaned_data['link'],
#                         prize = form.cleaned_data['prize'],
#                         mainboard = mainboard_instance,
#                         market = form.cleaned_data['market']
#                     )
#                     market_instance.save()

#             if request.FILES:
#                 for f in request.FILES.getlist('image'):
#                     img_instance = Image(image=f,mainboard=mainboard_instance)
#                     img_instance.save()
#         else:
#             print('Not successful')
#             # return the form with the previous data
#             return render(request,'forms/moth_form.html',context = {'info_form' : info_ret_form,'market_form':market_form})

#     context = {
#         'info_form' : mainboard_form,
#         'market_form' : market_form
#     }

#     return render(request,'forms/moth_form.html',context)