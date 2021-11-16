from django.urls import path 
from .views import *
app_name = 'exer'

urlpatterns = [
    path('exers/',exers,name='exers'),

]
