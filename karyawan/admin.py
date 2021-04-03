from django.contrib import admin
from karyawan.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'division']

admin.site.register(Employee, EmployeeAdmin)