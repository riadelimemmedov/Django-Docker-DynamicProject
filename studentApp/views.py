from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'students.html'#send all studends in students.html from databases
    context_object_name = 'students'