from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('sign-in/', views.index2, name='index2'),
    path('sign-in/homePage/', views.index3, name='index3'),
    path('NewStu/', views.index4, name='index4'),
    path('dep/', views.index5, name='index5'),
    path('upd/', views.index6, name='index6'),
    path('info/', views.index7, name='index7'),
    path('activ/', views.index8, name='index8'),
    path('table/', views.index9, name='index9'),
    path('prof/', views.index10, name='index10'),

]