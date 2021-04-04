from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from karyawan.views import *
from django.contrib.auth.views import LoginView
from karyawan.viewset_api import *
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('employee', EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', employee, name='employee'),
    path('add-employee/', add_employee, name='add_employee'),
    path('employee/edit_employee/<int:id_employee>', edit_employee, name='edit_employee'),
    path('employee/delete_employee/<int:id_employee>', delete_employee, name='delete_employee'),
    path('login/', LoginView.as_view(), name="login"),
    path('api/', include(routers.urls)),
]
