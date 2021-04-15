from django.db import models
from . items import Item


# Create your models here.
# class img(models.Model):
#     img = models.ImageField(null=True, blank=True)
#     item = models.ForeignKey(Item,on_delete=models.CASCADE)

class images(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Item,on_delete=models.CASCADE)
    image=models.FileField(max_length=255)
