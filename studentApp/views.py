from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'students.html'#send studends in students.html file
    context_object_name = 'students'