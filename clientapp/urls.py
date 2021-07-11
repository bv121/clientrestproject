 
from django.contrib import admin

from django.urls import path
from .views import *

urlpatterns = [
    path('createclient/',Createclient.as_view()),
    path('clientlist/',ClientList.as_view()),
    
    path('client/<int:pk>/',ClientDetail.as_view()),
    path('projectlist/',ProjectList.as_view()),
    path('project/<int:pk>/',ProjectDetail.as_view()),
    path('createproject/',ProjectCreate.as_view()),

]
