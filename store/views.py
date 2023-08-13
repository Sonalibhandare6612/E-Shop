from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Products, Category, Customer
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



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    else :
        postData = request.POST
        name = postData.get('name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        
        #keeping input data as it is after refresh page
        value = {
            'name' : name,
            'phone' : phone,
            'email' : email,
        }
        
        # Validation of input fields
        error_msg = None
        
        customer = Customer(cname=name, 
                            phone=phone, 
                            cemail=email, 
                            password=password)
        
        
        
        
        if(not name):
            error_msg = "Name reuired !!"
        elif len(name) < 4:
            error_msg = "Name should be more than 4 characters !!"    
        
        elif customer.isExistEmail():
            error_msg = 'Email allready registered'    
        # saving data
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("index")
            
        else :
            data = {
                'error' : error_msg,
                'values' : value
            }
            return render(request, "signup.html", data)
                
    



def order(request):
    return HttpResponse(request, "ITS order page")
