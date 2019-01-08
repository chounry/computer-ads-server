from django.contrib import admin
from .models import *
from django.db import models
from django.forms import Textarea

# Register your models here.
class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class MarketInline(admin.StackedInline):
    model = Mainboard_market
    extra = 1

class MainboradWidget(admin.ModelAdmin):
    formfield_overrides = {
       models.TextField : {'widget':Textarea(attrs={'rows':10,'cols':70})}
    }
    inlines = [ImageInline, MarketInline]

admin.site.register(Mainboard_info, MainboradWidget)
admin.site.register(Form_factor)
admin.site.register(Expansion_connector)
admin.site.register(Company)
admin.site.register(Chipset)
admin.site.register(Expansion_slot)

