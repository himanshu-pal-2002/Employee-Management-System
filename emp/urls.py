from django.urls import path
from emp.views import *

urlpatterns=[
    path('',index,name='index'),
]