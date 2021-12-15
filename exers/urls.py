from django.urls import path 
from .views import *
app_name = 'exer'

urlpatterns = [
    path('exers/',home,name='home'),
    path('add/',add_a_ex,name='add'),
    path('search/',SearchView.as_view(),name='search'),

]
