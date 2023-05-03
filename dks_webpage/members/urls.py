from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('jaya/', views.jaya, name='jaya'),
    path('teachers/', views.teachers, name='teachers'),
    path('button_pushed/', views.button_pushed, name='button_pushed'),
    path('button_pushed2/', views.button_pushed2, name='button_pushed2'),
    path('button_pushed3/', views.button_pushed3, name='button_pushed3'),
    path('statistics/', views.statistics, name='statistics'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('RATS/', views.RATS, name='RATS'),
    path('RAT2/', views.RAT2, name='RAT2'),
    path('RAT3/', views.RAT3, name='RAT3'),
    path('ALL_RATS/', views.ALL_RATS, name='ALL_RATS'),
]

