from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from market.models import Market_info
from ram.models import Mem_tech

class CPU_model(models.Model):
    name = models.CharField(help_text="Core i5 or Core i3",max_length=30)
    def __str__(self):
        return self.name

class Vertical_segment(models.Model):
    name = models.CharField("Vertical Segment",help_text="Desktop or Mobile",max_length=50)
    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField("Series",help_text="HQ or K",max_length=20)
    def __str__(self):
        return self.name

class Num_of_core(models.Model):
    amount = models.PositiveSmallIntegerField()
    name = models.CharField(blank=True, max_length=50,null=True)
    def __str__(self):
        if(self.name):
            return self.name + ' ' + str(self.amount)
        return str(self.amount)

class CPU_brand(models.Model):
    name = models.CharField("Brand Name",max_length=50)
    def __str__(self):
        return self.name

class Socket_type(models.Model):
    name = models.CharField("Socket Type",max_length=50)
    def __str__(self):
        return self.name

class CPU_info(models.Model):

    cpu_model = models.ForeignKey(CPU_model,on_delete=models.CASCADE)
    cpu_brand = models.ForeignKey(CPU_brand,on_delete=models.CASCADE)
    vertical_segment = models.ForeignKey(Vertical_segment,on_delete=models.CASCADE)
    series = models.ForeignKey(Series,on_delete=models.SET_NULL,null=True,blank=True)
    num_of_core = models.ForeignKey(Num_of_core,on_delete=models.CASCADE,verbose_name=u'# of Cores')
    socket_type = models.ForeignKey(Socket_type,on_delete=models.CASCADE)
    

    name = models.CharField(help_text="Ex: Intel Core i5-3470.",max_length=100)
    proc_num = models.CharField("Processor Number",help_text="3470 OR 860K OR FX-3202",max_length=30,null=True)
    cmos = models.CharField("CMOS",help_text='**Unit: nm or ELSE',max_length=50,default='---')
    num_of_thread = models.CharField("Number of Threads",max_length=100,blank=True,default='---')
    base_fr = models.CharField("Base Frequency",max_length=50,help_text='**Unit: GHz')
    cache = models.CharField("Cache",max_length=100,help_text='**Unit: MB',default='---')
    tdp = models.CharField("Power Consumtion",max_length=50,help_text='**Unit: W',default='---')
    max_memory = models.CharField(help_text='Unit: MB',max_length=100,blank=True,default='---')
    num_of_mem_chann = models.PositiveSmallIntegerField("# of Memory Channels")
    max_mem_bandwidth = models.CharField("Max Memory bandwidth",max_length=50,help_text='**Unit: MB/s or GB/s',blank=True,default='---')
    memory_tech = models.ManyToManyField(Mem_tech)
    slug = models.SlugField(unique=True,blank=True)
    
    class Meta:
        verbose_name = "CPU Info"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cpu:cpu_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.cpu_brand.name + ' ' + self.cpu_model.name + '-' + self.proc_num
        self.slug = slugify(self.name)
        super(CPU_info,self).save(*args,**kwargs)

class Image(models.Model):
    image = models.ImageField()

    cpu = models.ForeignKey(CPU_info,on_delete=models.CASCADE)

class CPU_market(models.Model):
    link = models.URLField(max_length=2000)
    prize = models.DecimalField(max_digits=7,decimal_places=2)
    
    cpu = models.OneToOneField(CPU_info,on_delete=models.CASCADE)
    market = models.ForeignKey(Market_info,on_delete=models.CASCADE)

    
