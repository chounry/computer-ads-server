from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse

from mainboard.models import Expansion_slot
from market.models import Market_info
from comSpec import myUtil

class API_supp(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=10,blank=True,default=' ')
    def __str__(self):
        tmp = self.version if self.version else ''
        return self.name + tmp
    
    class Meta:
        verbose_name = 'API Support'

class GPU_brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'GPU Brand'

class Vram_type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class GPU(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Processor(models.Model):
    name = models.CharField(max_length=50,help_text="Stream Processor or CUDA or else")
    def __str__(self):
        return self.name

class Graphic_info(models.Model):
    """
    mem_speed : don't forget to put the unit behind it after a space; eg. 1350 MHz or 114 MB/s 
    """
    gpu_brand = models.ForeignKey(GPU_brand,on_delete=models.CASCADE,verbose_name='GPU Brand')
    gpu = models.ForeignKey(GPU,on_delete=models.CASCADE,verbose_name="GPU",help_text='eg:nVidia or AMD')
    processor = models.ForeignKey(Processor,on_delete=models.CASCADE,help_text='eg:CUDA or Stream', null=True, blank=True)

    name = models.CharField(max_length=100,blank=True,help_text="Do not include Manufactur Name")
    model_num = models.CharField(max_length=100,blank=True, default='---')
    core_clock = models.CharField(help_text="**Unit :MHz",max_length=50,blank=True,default='---')
    boost_clock = models.CharField(help_text='**Unit :MHz',max_length=50,blank=True,default='---')
    mem_cap = models.PositiveIntegerField("Memory Capacity",help_text='Unit: MB')
    mem_inter_width = models.CharField("Memory Interface Width",max_length=10,help_text="**eg:128 or 256,Unit :bit)")
    num_of_core = models.PositiveIntegerField("# Number of Cores",null=True,blank=True)
    mem_speed = models.CharField(help_text="**unit: MB/s or MHz",max_length=50,blank=True,default='---')
    mem_bandwidth = models.CharField("Memory Bandwidth",max_length=50,help_text='**Unit: MB/s or GB/s',blank=True,default='---')
    vram_type = models.ForeignKey(Vram_type,on_delete=models.CASCADE,verbose_name=u'Vram Type')
    power = models.CharField(max_length=30,help_text='**Unit: W',blank=True,default='---')
    recom_power = models.CharField("Recommending Power", max_length=30,help_text='**Unit: W',blank=True,default='---')
    dimension = models.CharField('Product Dimension', max_length=50,blank=True,default='---')
    slug = models.SlugField(unique=True,blank=True,max_length=500)

    api_supp = models.ManyToManyField(API_supp,verbose_name='API Support',help_text='eg:DirectX')
    expansion_slot = models.ForeignKey(Expansion_slot, on_delete=models.CASCADE,verbose_name=u'Expansion Connector')

    def get_mem_cap(self):
        return str(self.mem_cap)+' MB' if len(str(self.mem_cap)) < 4 else str(myUtil.toGBint(self.mem_cap)) + ' GB'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('graphic:graphic_detail',kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if not self.slug:
            # if there is no slug, it means this is a first save
            self.power = self.power.upper()

            tmp_name = self.name if self.name else ''
            tmp_mem_cap = self.get_mem_cap()
            self.name = self.gpu_brand.name +' ' + tmp_name + ' ' + tmp_mem_cap + ' ' + self.vram_type.name
            self.slug = slugify(self.name+' '+self.model_num+' ')       
        super(Graphic_info,self).save(*args,**kwargs) 

class Image(models.Model):
    image = models.ImageField(upload_to='graphic')

    graphic = models.ForeignKey(Graphic_info,on_delete=models.CASCADE)

class Graphic_market(models.Model):
    link = models.URLField(max_length=2000)
    prize = models.DecimalField(max_digits=7,decimal_places=2)    

    graphic = models.ForeignKey(Graphic_info,on_delete=models.CASCADE)
    market = models.OneToOneField(Market_info,on_delete=models.CASCADE)

