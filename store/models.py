from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length= 255)

    def __str__(self) -> str:
        return self.first_name

class Restaurant(models.Model):
    name = models.CharField(max_length= 100)
    description = models.CharField(max_length = 255)
    location = models.CharField(max_length= 255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']

class Menu(models.Model):
    title= models.CharField(max_length= 255)
    restaurant = models.ForeignKey(Restaurant,related_name= 'menus',on_delete=models.CASCADE)
    description = models.CharField(max_length = 255)

    def __str__(self):
        return self.title

class MenuItems(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length= 255)
    price = models.DecimalField(max_digits=5,decimal_places= 2)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)

class Order(models.Model):
    STATUS_CHOICES =[
        ('placed','Placed'),
        ('in_progress','In Progress'),
        ('deliverd','Deliverd')
    ]
    customer = models.ForeignKey(Customer,on_delete= models.CASCADE)
    items = models.ManyToManyField(MenuItems)
    total_price = models.DecimalField(max_digits=5,decimal_places = 2)
    status = models.CharField(max_length=20,choices = STATUS_CHOICES,default='placed')
    created_at = models.DateTimeField()
    
    def calculate_total_price(self):
       total_price = sum(item.price for item in self.items.all())
       self.total_price = total_price
       self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.calculate_total_price()


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    item_id = models.ForeignKey(MenuItems,on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()





