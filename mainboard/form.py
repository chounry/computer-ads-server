from django import forms
from dal import autocomplete
from .models import *

class MainboardForm(forms.ModelForm):

    class Meta:
        model = Mainboard_info
        exclude = ['slug']
        widgets = {
            'form_factor':autocomplete.ModelSelect2(url='mainboard:form-factor-ac'),
            'company': autocomplete.ModelSelect2(url='mainboard:company-ac'),
            'socket_type':autocomplete.ModelSelect2(url='mainboard:socket-type-ac'),
            'chipset':autocomplete.ModelSelect2(url='mainboard:chipset-ac'),
            'expan_slot':forms.SelectMultiple(
                attrs={'class':'selectpicker','data-live-search':'true','data-actions-box':'true'}
                )
        }

class MainboardMarketForm(forms.ModelForm):

    class Meta:
        model = Mainboard_market
        fields = '__all__'
        widgets = {
            'market':forms.Select(attrs={'class':'selectpicker mb-3','data-width':'100%'})
        }
    
class MainboardImgForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
    