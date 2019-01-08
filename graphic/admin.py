from django.contrib import admin
from django.forms import Textarea
from .models import *

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class MarketInline(admin.StackedInline):
    model = Graphic_market
    extra = 1

class GraphicWidget(admin.ModelAdmin):
   formfield_overrides = {
      models.TextField : {'widget':Textarea(attrs={'rows':10,'cols':70})}
   }
   inlines = [ImageInline, MarketInline]

# Register your models here.
admin.site.register(Graphic_info, GraphicWidget)
admin.site.register(GPU)
admin.site.register(GPU_brand)
admin.site.register(API_supp)
admin.site.register(Vram_type)
admin.site.register(Processor)
