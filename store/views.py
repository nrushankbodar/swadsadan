from django.shortcuts import get_object_or_404
from django.db.models import  Value,F, Func
from django.core.exceptions import ObjectDoesNotExist
from .models import Restaurant,Menu
from rest_framework import status
from .serializers import RestaurantSerializer,MenuSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def Restaurant_list(request):
    if request.mehtod == 'GET':
       queryset =Restaurant.objects.all()
       serializer= RestaurantSerializer(queryset,many=True)
       return Response(serializer.data)
    
     
@api_view(['GET','POST'])
def menu_list(request, id):
    if request.method=='GET':
       menu= Menu.objects.get(pk=id)
       serializer= MenuSerializer(menu)
       return Response(serializer.data)
    elif request.method=='POST':
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')
    

    
    