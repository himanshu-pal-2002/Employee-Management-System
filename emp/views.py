from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee,Role,Department

# Create your views here.
def index(request):
    return render(request,'emp/index.html')

def All_Emp(request):
    emps=Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'emp/view_all_emp.html',context)

def Add_Emp(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        hire_date=request.POST['hire_date']
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,
                         phone=phone,hire_date=hire_date)
        new_emp.save()
        return HttpResponse('Employee added Successfully')
        
    elif request.method=='GET':
        return render(request,'emp/add_emp.html')
    
    else:
        return HttpResponse('An exception occured Employee Has not added')

def Remove_Emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed Successfully')
        except:
            return HttpResponse('Please Enter a Valid Emp Id')
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'emp/remove_emp.html',context)

def Filter_Emp(request):
    return render(request,'emp/filter_emp.html')