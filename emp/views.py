from django.shortcuts import render
from .models import Employee,Role,Department

# Create your views here.
def index(request):
    return render(request,'emp/index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'emp/view_all_emp.html',context)

def add_emp(request):
    return render(request,'emp/add_emp.html')

def remove_emp(request):
    return render(request,'emp/remove_emp.html')

def filter_emp(request):
    return render(request,'emp/filter_emp.html')