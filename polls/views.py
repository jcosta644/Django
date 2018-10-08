from django.shortcuts import render
from django.http import HttpResponse

from .models import Subject


def index(request):
    output = ', '.join([s.nameSubject for s in Subject.objects])
    return HttpResponse(output)


def detail(request, idSubject):
    return HttpResponse("You're looking at Subject %s." % idSubject)
