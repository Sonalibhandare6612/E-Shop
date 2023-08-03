from django.contrib import admin
from store.models import Products, Category



class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    

class AdminCategory(admin.ModelAdmin):  
    list_display = ['name']  
    

# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category, AdminCategory)
