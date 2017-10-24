from django.shortcuts import render
from django.views.generic import CreateView,DeleteView
from basic_app2 import models
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class StudentCreateView(CreateView):
    fields = ('name','age','school')
    model = models.Student


class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("basic_app:list")

