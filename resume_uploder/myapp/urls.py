from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('candidate/<int:pk>',views.Candidate,name='candidate'),
]