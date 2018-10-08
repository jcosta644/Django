from django.db import models


class Subject(models.Model):
    nameSubject = models.CharField(max_length=200)
    levelSubject = models.CharField(max_length=200)
    areaSubject = models.CharField(max_length=200)