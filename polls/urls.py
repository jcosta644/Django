from django.urls import path

from . import views

urlpatterns = [
    path('', views.subjectList.as_view(), name='subject_list'),
    path('add', views.subjectCreate.as_view(), name='subject_create'),
    path('view/<int:pk>', views.subjectView.as_view(), name='subject_view'),
    path('update/<int:pk>', views.subjectUpdate.as_view(), name='subject_update'),
    path('delete/<int:pk>', views.subjectDelete.as_view(), name='subject_delete'),
]