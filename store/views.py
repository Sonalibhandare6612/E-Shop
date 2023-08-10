from django.shortcuts import render, HttpResponse
from .models import Products, Category
from . import models

# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
        
    else:
        products = Products.get_all_products()    
        
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, "index.html",data)



def order(request):
    return HttpResponse(request, "ITS order page")
