from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from cpu.models import Socket_type,CPU_info
from ram.models import Mem_tech,Memory_info
from market.models import Market_info

class Form_factor(models.Model):
    name = models.CharField("Form Factor",max_length=50)

    def __str__(self):
        return self.name

#---- this for other table also -----
class Expansion_connector(models.Model):
    name = models.CharField(help_text="eg: PCI or PCIe or ...",max_length=30)
    version = models.DecimalField(max_digits=3,decimal_places=1)
    def __str__(self):
        return self.name + ' ' + str(self.version)

class Chipset(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Expansion_slot(models.Model):
    expansion_conn = models.ForeignKey(Expansion_connector,on_delete=models.CASCADE)
    pin = models.CharField(max_length=10,blank=True,default=' ')
    
    def __str__(self):
        tmp = self.pin if self.pin else ''
        return self.expansion_conn.name + ' ' + str(self.expansion_conn.version) + ' ' + tmp 

class Mainboard_info(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    form_factor = models.ForeignKey(Form_factor,on_delete=models.CASCADE)
    socket_type = models.ForeignKey(Socket_type,on_delete=models.CASCADE)
    chipset = models.ForeignKey(Chipset,on_delete=models.CASCADE)

    name = models.CharField(max_length=100, help_text="Mainboard's name")
    cpu_des = models.TextField("CPU Description",max_length=300,default='---')
    size = models.CharField(max_length=250,help_text='eg : 30.5cm x 24.4cm')
    storage_des = models.TextField("Storage Description",max_length=500,default='---')
    multi_gpu_des = models.TextField("Multi GPU",default='---')
    #  *************************
    memmory_des = models.TextField("Memory Description",max_length=500) # memory not memmory
    rear_panel_des = models.TextField("Rear Panel Description",max_length=1500)
    expand_slot_des = models.TextField("Expansion Slot Description",max_length=2000)
    audio_des = models.TextField("Audio Description",max_length=1000,default='---')
    interal_des = models.TextField("Interal I\O Connector",max_length=1500)
    onboard_gpu_des = models.TextField("On Board GPU",max_length=40,default='---')
    slug = models.SlugField(unique=True,blank=True)

    expan_slot = models.ManyToManyField(Expansion_slot,verbose_name='Expansion Slot')

    def __str__(self):
        return self.company.name + ' ' + self.name + ' ' + self.socket_type.name

    def get_absolute_url(self):
        return reverse('mainboard:mainboard_detail', kwargs={"slug": self.slug})

    def save(self,*args,**kwargs):   
        self.slug = slugify(self.company.name + ' ' + self.name + ' ' +self.socket_type.name)     
        super(Mainboard_info,self).save(*args,**kwargs)

class Image(models.Model):
    image = models.ImageField(upload_to='mainboard')

    mainboard = models.ForeignKey(Mainboard_info,on_delete=models.CASCADE)

class Mainboard_market(models.Model):
    link = models.URLField(max_length=2000)
    prize = models.DecimalField(max_digits=7,decimal_places=2) # prize not prize

    mainboard = models.ForeignKey(Mainboard_info,on_delete=models.CASCADE)
    market = models.OneToOneField(Market_info,on_delete=models.CASCADE)

    



