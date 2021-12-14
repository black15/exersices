from django.shortcuts import render,redirect
from .forms import AddAnAexerForms
# Create your views here.
from .models import * 
def home(request):
    return render(request,'home.htm')
'''
@api_view(['POST','GET'])
def exers(request):
    print('@@@@@@@@@@@@@@@@@@@')

    print(request)
    print('@@@@@@@@@@@@@@@@@@@')
    if request.method=="GET":
        data = Exer.objects.all()
        serializer = ExerSerializer(data,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        q = request.data.get('q')
        with_solution=not request.data.get('with_solution')
        print(with_solution)
        data = Exer.objects.filter(subject_name__icontains=q).exclude(solution=with_solution)
#        data2 = Exer.objects.filter(name__icontains=q).exclude(solution=with_solution)

        serializer = ExerSerializer(data,many=True)
        return Response(serializer.data)

'''
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