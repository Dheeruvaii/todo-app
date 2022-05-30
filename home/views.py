from urllib import response
from django.shortcuts import render,HttpResponse
from rest_framework import generics
from rest_framework import viewsets
from .serializers import todoserializers
from .models import *

# Create your views here.
class listtodo(viewsets.ModelViewSet):
    queryset=todo.objects.all()
    serializer_class=todoserializers
    
class Detailtodo(generics.RetrieveUpdateAPIView):
    queryset=todo.objects.all()
    serializer_class=todoserializers

class Createtodo(generics.CreateAPIView):
    queryset=todo.objects.all()
    serializer_class=todoserializers
    
    
    
class Deletetode(generics.DestroyAPIView):
    queryset = todo.objects.all()
    serializer_class=todoserializers
    
class UpdateTodo(generics.UpdateAPIView):
    queryset = todo.objects.all()
    serializer_class=todoserializers
    
 