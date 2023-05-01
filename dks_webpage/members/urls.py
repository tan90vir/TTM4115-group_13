from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('jaya/', views.jaya, name='jaya'),
    path('statistics/', views.statistics, name='statistics'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('RATS/', views.RATS, name='RATS'),
    path('RAT2/', views.RAT2, name='RAT2'),
    path('RAT3/', views.RAT3, name='RAT3'),
    path('ALL_RATS/', views.ALL_RATS, name='ALL_RATS'),
]

