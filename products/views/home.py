from django.shortcuts import render
from django.http import HttpResponse
from products.models.departments import Department
# Create your views here.
def index(request):
    department = Department.objects.filter(active=1)
    return render(request,'home/index.html',{'all_departments':department})
    # return HttpResponse('hello my name is donso')