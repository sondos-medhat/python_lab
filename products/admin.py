from django.contrib import admin
# from .models import Department,Item

from products.models.departments import Department
from products.models.items import Item


admin.site.register(Department)
admin.site.register(Item)

# Register your models here.


