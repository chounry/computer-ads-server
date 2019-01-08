from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from .form import *
from .models import *

# Create your views here.

def get_all_cpu(request):
    all_cpu = CPU_info.objects.all()
    context = {"all_cpus": all_cpu}
    return render(request, "cpu/cpu_pro_list.html", context)

def get_cpu_detail(request, slug):
    cpu = get_object_or_404(CPU_info, slug=slug)
    context = {
        "cpu": cpu
    }
    return render(request, 'cpu/cpu_detail.html', context)












# def handle_form(request):
#     cpu_form = CPUForm()
#     market_form = CPUMarketForm()['market']    

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

#             MarketFormset = modelformset_factory(CPU_market,form=CPUMarketForm)
#             m_formset = MarketFormset(data)
#             market_valid = m_formset.is_valid()

#         info_ret_form = CPUForm(request.POST)
#         print(m_formset.errors)
#         print(market_valid)
#         if info_ret_form.is_valid() and market_valid:
#             cpu_instance = info_ret_form.save()
            
#             # if the market formset availble 
#             if m_formset:
#                 for form in m_formset:
#                     market_instance = CPU_market(
#                         link  = form.cleaned_data['link'],
#                         prize = form.cleaned_data['prize'],
#                         cpu = cpu_instance,
#                         market = form.cleaned_data['market']
#                     )
#                     market_instance.save()

#             if request.FILES:
#                 for f in request.FILES.getlist('image'):
#                     img_instance = Image(image=f,cpu=cpu_instance)
#                     img_instance.save()
#         else:
#             print('Not successful')
#             # return the form with the previous data
#             return render(request,'forms/pro_form_base.html',context = {'info_form' : info_ret_form,'market_form':market_form})

#     context = {
#         'info_form' : cpu_form,
#         'market_form' : market_form
#     }

#     return render(request,'forms/pro_form_base.html',context)