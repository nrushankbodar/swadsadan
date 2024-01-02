from rest_framework import serializers
from store.models import Restaurant,Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields= '__all__'
   
   
    
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [ 'id','name','location']
    # id= serializers.IntegerField()
    # name = serializers.CharField(max_length= 100)
    # location= serializers.CharField(max_length= 200)

  
