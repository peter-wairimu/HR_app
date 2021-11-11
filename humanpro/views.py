from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def index(request):
    employees = Employee.objects.order_by('id').all()
    return render(request, 'human/index.html', {'employees': employees})
