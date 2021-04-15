from django.core.files.storage import FileSystemStorage
from django.core.mail.backends import console
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse,HttpRequest
from products.models.departments import Department
from products.models.items import Item
from products.models.images import images
from django.core.serializers import serialize, json
import os
import requests


# Create your views here.
def index(request):

    # image = images.objects.all()
    # item = Item.objects.all()
    # return render(request,'item/index.html',{'all_items':item,'all_images':image})
    # data = serialize("json", item)
    # return HttpResponse(data)

    url = 'https://cp-dev.eq.ademo.net/public/api/admin/employee/list'
    data = requests.get(url)
    mydata = data.json()
    item =mydata['data']['EmployeesData']


    return render(request,'item/index.html',{'all_items': item})


def read(request,item_id):

    #item = get_object_or_404(Item,id=item_id).first()
   #  item = Item.objects.filter(id=item_id)
   # # image = images.objects.all()
   #  data = serialize("json", item)
   #  return HttpResponse(data,content_type="application/json")

    data = requests.get('https://cp-dev.eq.ademo.net/public/api/admin/employee/show/' + item_id)
    geodata = data.json()
    item = geodata['data']['EmployeesData']
    return render(request, 'item/read.html', {'item_data': item})


def create(request):
    if request.method == "GET":
        # list departments
        departments = Department.objects.all()

        return render(request, 'item/add.html', {'all_departments' : departments})
    else:
        visableres = json.loads('visable')
        if visableres == 'on':
            result=True
        else:
            result=False

        all_departments = Department.objects.filter(id__in=json.loads('department_id'))
        instance = Item.objects.create(
            name=json.loads('name'), description=json.loads('description'),
            price=json.loads('price'),visableres=True)

        instance.department.set(all_departments)
# multiple images
#         image = request.FILES.getlist("file[]")
#         for img in image:
#             fs = FileSystemStorage()
#             file_path = fs.save(img.name, img)
#
#             pimage = images(product_id=instance, image=file_path)
#             pimage.save()



        return redirect('item_list')
        # console.log(selected_department)


def delete(request, item_id):
    url="https://cp-dev.eq.ademo.net/public/api/admin/employee/delete/{id}"

    data = requests.get(url)
    mydata = data.json()
    item = mydata['data']['EmployeesData']

    # item = Item.objects.filter(id=item_id)
    # #item = get_object_or_404(Item, id=item_id)
    # item.delete()

    #item.destroy()
    return redirect('item_list')

    # return redirect('item_list')



def edit(request, item_id):
    if request.method == "GET":
        item = get_object_or_404(Item, id=item_id)
        all_departments = Department.objects.all()
        return render(request, "item/edit.html", {"item": item, "all_departments": all_departments} )
    else:
        item = Item.objects.get(id=item_id)
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        # image = None
        image=request.POST.get('image')


        all_departments = Department.objects.filter(id__in=request.POST.getlist('department_id'))
        if name:
            item.name = name
        if description:
            item.description = description
        if price:
            item.price = price

        if all_departments:
            item.department.set(all_departments)
        if request.FILES:
            image = request.FILES['image']
        if image:
            item.img= image
            # item.image.img= image

        item.save()
        return redirect('item_list')

def filter(request, dept_id):
    item = Item.objects.filter(department=dept_id).all()
    image = images.objects.all()
    return render(request, 'item/filter.html', {'item': item,'all_images':image})

