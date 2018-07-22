from django.db import models

# Create your models here
class Market_info(models.Model):
    market_name = models.CharField(max_length=50)
    img = models.ImageField(max_length=200)

    def __str__(self):
        return self.market_name
