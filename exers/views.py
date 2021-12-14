from django.shortcuts import render
from rest_framework.response import Response
import datetime
from itertools import chain
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ExerSerializer
# Create your views here.
from .models import * 
def home(request):
    return render(request,'index.htm')

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

@api_view(['POST'])

def add_a_ex(request):
    if request.method=='POST':
        ex_file = request.FILES.get('ex_file')
        sou_file = request.FILES.get('sou_file')
        print(ex_file)
        print(sou_file)
        serializer = ExerSerializer(data=request.data,Files=request.FILES)

        data={}
        data['msg']=False
        if serializer.is_valid():
            serializer.save()
            data['msg']=True
            return Response(data)
        return Response(data)