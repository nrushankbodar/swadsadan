from django.urls import path
from .import views

urlpatterns = [
    path('restaurants/',views.Restaurant_list),
    path('menus/<int:id>/',views.menu_list)
]
