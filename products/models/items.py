from django.db import models
from . departments import Department
# from . images import images

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price =models.DecimalField(max_digits=6,decimal_places=2)

    # photo=models.FileField(upload_to="post_image",blank=True)
    # //only 1 img
    # img = models.ImageField(null=True,blank=True)
    # multiple images
    # img = models.ForeignKey(images,on_delete=models.CASCADE,blank=True,null=True)
    # many to many

    # //one to many
    # department=models.ForeignKey(Department,on_delete=models.CASCADE)
    # many to many
    department = models.ManyToManyField(Department)

    visable=models.BooleanField(default=False)
    # class Meta:
    #     db_table = "item"


    def __str__ (self):
        return self.name
