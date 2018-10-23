from django.db import models
from django.urls import reverse


class Subject(models.Model):
    nameSubject = models.CharField(max_length=200)
    levelSubject = models.CharField(max_length=200)
    areaSubject = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})