from django.shortcuts import render,redirect
from .forms import AddAnAexerForms
from django.db.models import Q
from django.views.generic import ListView

# Create your views here.
from .models import *

def home(request):
    context = {}

    exercises = Exer.objects.all()

    context['exercises'] = exercises
    return render(request,'exers/home.html', context)


def add_a_ex(request):
    form = AddAnAexerForms()
    if request.method =='POST':
        form = AddAnAexerForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("exers:add")
    context = {
        'form' : form

    }
    return render(request,'exers/add.html',context)

class SearchView(ListView):

    model = Exer
    template_name = 'exers/home.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('q')
       if query:
          postresult = Exer.objects.filter(name__contains=query)
          result = postresult
       else:
           result = None
       return result