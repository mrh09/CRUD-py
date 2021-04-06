from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from karyawan.models import Employee
from karyawan.forms import FormEmployee
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template import loader
from django.http import HttpResponse

def gettemplate(request):
    template = loader.get_template('registration/login.html')

    return HttpResponse(template.render)

class LandingView(TemplateView):
    template_name = 'registration/login.html'

@login_required(login_url=settings.LOGIN_URL)
def delete_employee(request, id_employee):
    employee = Employee.objects.filter(id=id_employee)
    employee.delete()

    return redirect('employee')

@login_required(login_url=settings.LOGIN_URL)
def edit_employee(request, id_employee):
    employee = Employee.objects.get(id=id_employee)
    template = 'edit-employee.html'
    if request.POST:
        form = FormEmployee(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "data has been changed successfully!")
            return redirect('edit_employee', id_employee=id_employee)
    else:
        form = FormEmployee(instance=employee)
        konteks = {
            'form' : form,
            'employee' : employee,
        }
            
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def employee(request):
    employees = Employee.objects.all()

    konteks = {
        'employees' : employees,
    }

    return render(request, 'employee.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def add_employee(request):
    if request.POST:
        form = FormEmployee(request.POST)
        if form.is_valid:
            form.save()
            form = FormEmployee()
            message = "Data Saved Successfully "

            konteks = {
            'form' : form,
            'message' : message, 
        }

        return render(request, 'add-employee.html', konteks)

    else:
        form = FormEmployee()

        konteks = {
            'form' : form,
        }

        return render(request, 'add-employee.html', konteks)

# Create your views here.
