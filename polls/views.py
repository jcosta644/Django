from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Subject


class subjectList(ListView):
    model = Subject


class subjectCreate(CreateView):
    model = Subject
    fields = ['nameSubject', 'levelSubject', 'areaSubject']
    success_url = reverse_lazy('subject_list')


class subjectView(DetailView):
    model = Subject


class subjectUpdate(UpdateView):
    model = Subject
    fields = ['nameSubject', 'levelSubject', 'areaSubject']
    success_url = reverse_lazy('subject_list')


class subjectDelete(DeleteView):
    model = Subject
    success_url = reverse_lazy('subject_list')