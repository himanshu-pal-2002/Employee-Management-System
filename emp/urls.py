from django.urls import path
from emp.views import *

urlpatterns=[
    path('',index,name='index'),
    path('All_Emp',All_Emp,name='All_Emp'),
    path('Add_Emp',Add_Emp,name='Add_Emp'),
    path('Remove_Emp',Remove_Emp,name='Remove_Emp'),
    path('Remove_Emp/<int:emp_id',Remove_Emp,name='Remove_Emp'),
    path('Filter_Emp',Filter_Emp,name='Filter_Emp'),
]