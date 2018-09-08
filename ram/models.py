from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from comSpec import myUtil

from market.models import *

class Mem_tech(models.Model):
    name = models.CharField(max_length=50)
    mem_type = models.CharField(help_text='eg: SDRAM',max_length=30,null=True,default=' ')
    def __str__(self):
        return self.name + ' ' + self.mem_type

class Mem_brand(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class Module_type(models.Model):
    module_name = models.CharField("Module Name",max_length=50)
    cycle_time = models.CharField(max_length=50,help_text='**Unit: ns',null=True,blank=True)
    transfer_time = models.CharField(max_length=50,help_text='**Unit: ns',null=True,blank=True)
    command_rate = models.CharField(max_length=50,help_text='**Unit: MHz')

    def __str__(self):
        return self.module_name + ' ' + self.command_rate
class Form_factor(models.Model):
    name = models.CharField(help_text='eg: SO-DIMM',max_length=30)    

    def __str__(self):
        return self.name

class Pin(models.Model):
    num_of_pin = models.PositiveSmallIntegerField()
    form_factor = models.ForeignKey(Form_factor,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.num_of_pin)+ '-pin ' + self.form_factor.name

class Memory_info(models.Model):
    platform_choice = (('Desktop','Desktop'),('Laptop','Laptop'))
    ecc_choice = (('Yes','Yes'), ('No','No'))

    module_type = models.ForeignKey(Module_type,on_delete=models.SET_NULL,null=True,blank=True)

    platform = models.CharField(max_length=10,choices=platform_choice,null=True)
    isECC = models.CharField(max_length=3, choices=ecc_choice,blank=True,default='---')
    series = models.CharField(max_length=50, default=' ', blank=True)
    model_num = models.CharField("Item Model Number",blank=True,max_length=100,default='---')
    capacity = models.PositiveIntegerField(help_text="Unit: MB")
    slug = models.SlugField(unique=True,blank=True,max_length=100)
    voltage = models.CharField(max_length=100,help_text="**Unit: V",blank=True,default='---')
    pin = models.ForeignKey(Pin,on_delete=models.SET_NULL, null=True)

    mem_brand = models.ForeignKey(Mem_brand,on_delete=models.CASCADE,verbose_name='Memory Brand')
    mem_tech = models.ForeignKey(Mem_tech,on_delete=models.CASCADE,verbose_name='Memory Technology')

    def get_mem_cap(self):
        return str(self.capacity)+' MB' if len(str(self.capacity)) < 4 else str(myUtil.toGBint(self.capacity)) + ' GB'

    def get_absolute_url(self):
        return reverse('ram:ram_detail',kwargs={'slug': self.slug})

    def save(self,*args,**kwargs):
        # tmp for preventing null value
        if not self.slug:
            tmp_module_name = self.module_type.module_name if self.module_type else ' '
            tmp_model_num = self.model_num if self.model_num else ' '
            self.slug = slugify("%s %s %s %d %s"%(self.mem_brand.name, tmp_model_num, tmp_module_name, self.capacity, self.series))
        super(Memory_info, self).save(*args,**kwargs)

    def __str__(self):
        return self.mem_brand.name+ ' '+ self.series + ' ' + self.mem_tech.name + ' ' + self.get_mem_cap()+ ' '  + self.model_num

class Image(models.Model):
    image = models.ImageField(upload_to='ram')
    ram = models.ForeignKey(Memory_info,on_delete=models.CASCADE)

class Memory_market(models.Model):
    link = models.URLField(max_length=2000)
    prize = models.DecimalField(max_digits=7,decimal_places=2)  
    quntity = models.PositiveSmallIntegerField()  

    memory = models.ForeignKey(Memory_info,on_delete=models.CASCADE)
    market = models.OneToOneField(Market_info,on_delete=models.CASCADE)