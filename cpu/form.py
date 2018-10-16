from django import forms
from dal import autocomplete
from .models import *


class CPUForm(forms.ModelForm):
    class Meta:
        model = CPU_info
        exclude = ['slug']
        widgets = {
            'cpu_model':autocomplete.ModelSelect2(url='cpu:cpu_model-ac'),
            'cpu_brand':autocomplete.ModelSelect2(url='cpu:cpu_brand-ac'),
            'vertical_segment': autocomplete.ModelSelect2(url='cpu:vertical_segment-ac'),
            'socket_type': autocomplete.ModelSelect2(url='cpu:socket-type-ac'),
            'series':autocomplete.ModelSelect2(url='cpu:series-ac'),
            'num_of_core':autocomplete.ModelSelect2(url='cpu:num-of-cores-ac'),
            'memory_tech':forms.SelectMultiple(
                attrs={'class':'selectpicker','data-live-search':'true','data-actions-box':'true'}
            )
        }
class CPUMarketForm(forms.ModelForm):
    class Meta:
        model = CPU_market
        exclude = ['cpu']



