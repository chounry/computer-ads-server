from django.contrib import admin
from django.forms import Textarea
from .models import *

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class MarketInline(admin.StackedInline):
    model = Memory_market
    extra = 1

class RamWidget(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : {'widget':Textarea(attrs={'rows':10,'cols':40})}
    }
    inlines = [ImageInline, MarketInline]


# Register your models here.
admin.site.register(Module_type)
admin.site.register(Memory_info, RamWidget)
admin.site.register(Pin)
admin.site.register(Form_factor)
admin.site.register(Mem_brand)
admin.site.register(Mem_tech)