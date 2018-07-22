from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import *

# Register your models here.
class CPUwidget(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : {'widget':Textarea(attrs={'rows':10,'cols':40})}
    }

admin.site.register(CPU_info)
admin.site.register(CPU_brand)
admin.site.register(CPU_model)
admin.site.register(Vertical_segment)
admin.site.register(Series)
admin.site.register(Socket_type)
admin.site.register(Num_of_core)
