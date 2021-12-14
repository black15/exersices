from django.urls import path 
from .views import *
app_name = 'exer'

urlpatterns = [
    path('exers/',exers,name='exers'),
    path('exer-add/',add_a_ex,name='exter_add')

]
