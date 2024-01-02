from django.contrib import admin
from .import models 


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display= ['first_name','last_name','email','address']
# Register your models here.
    
@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_diplay  = ['title','restaurant','description']
    

@admin.register(models.Restaurant)
class restaurantAdmin(admin.ModelAdmin):
    list_display= ['name','description','location']

@admin.register(models. MenuItems)
class MenuItemAdmin(admin.ModelAdmin):
    list_display=['name','description','price','menu']
