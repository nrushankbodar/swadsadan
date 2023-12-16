from django.db import models

# Create your models here.

class User(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    address = models.CharField(max_length= 255)

class Restaurant(models.Model):
    name = models.CharField(max_length= 100)
    description = models.CharField(max_length = 255)
    location = models.CharField(max_length= 255)

class Menu(models.Model):
    title= models.CharField(max_length= 255)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    descreption = models.CharField(max_length = 255)

class MenuItems(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length= 255)
    price = models.DecimalField(max_digits=4,decimal_places= 2)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)

class Order(models.Model):
    STATUS_CHOICES =[
        ('placed','Placed'),
        ('in_progress','In Progress'),
        ('deliverd','Deliverd')
    ]
    user_id = models.ForeignKey(User,on_delete= models.CASCADE)
    order_date= models.DateField(auto_now_add = True)
    status = models.CharField(max_length=20,choices = STATUS_CHOICES,default='placed')

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    item_id = models.ForeignKey(MenuItems,on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()





