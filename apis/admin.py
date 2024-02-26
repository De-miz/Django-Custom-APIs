from django.contrib import admin
from .models import *

# Register your models here.


class MyRecipeBook_Admin(admin.ModelAdmin): 
    
    list_display = ['dish_name', 'primary_image_url', 'images_url', 'ingredients']
    
    
    
admin.site.register(MyRecipeBook, MyRecipeBook_Admin)