from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Products, Category, Customer
from . import models
from django.views import View

# Create your views here.
class Index(View):
    def post(self):
        return redirect("index")
    
    
    
    
    def get(self, request):
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

        
        
        
        


    
    
class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData = request.POST
        cname = postData.get('cname')
        phone = postData.get('phone')
        cemail = postData.get('cemail')
        password = postData.get('password')
        
    #keeping input data as it is after refresh page
        value = {
        'cname' : cname,
        'phone' : phone,
        'cemail' : cemail,
        }      
        error_msg = None    
        customer = Customer(cname=cname, 
                            phone=phone, 
                            cemail=cemail, 
                            password=password)
    
        error_msg =  self.validateCustomer(customer)
        
        
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
    
    def validateCustomer(self,customer):
        error_msg = None
        if(not customer.cname):
            error_msg = "Name required !!"
        elif len(customer.cname) < 4:
            error_msg = "Name should be more than 4 characters !!"    
        if(not customer.phone):
            error_msg = "phone reuired !!"
        elif len(customer.phone) < 10:
            error_msg = "phone should be more than 10 integers !!"    
        if(not customer.cemail):
            error_msg = "email reuired !!"
        elif len(customer.cemail) < 5:
            error_msg = "email should be more than 5 characters !!"    
        if(not customer.password):
            error_msg = "password reuired !!"
        elif len(customer.password) < 6:
            error_msg = "password should be more than 6 integers !!"        
        elif customer.isExistEmail():
            error_msg = 'Email allready registered' 
        return error_msg    
        


def order(request):
    return HttpResponse(request, "ITS order page")


# Creating Class based view for login
class Login(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        cemail = request.POST.get('cemail')
        password = request.POST.get('password')
        loginuser = Customer.get_customer_by_email(cemail)
        error_msg = None
        if loginuser:
            flag = check_password(password, loginuser.password)
            if flag:
                request.session['loginuser'] = loginuser.id
                logoutflag = True
                return redirect("index", {'logoutflag':logoutflag})
            else:
                error_msg = "Invalid password !"
        else:
            error_msg = "User not found !"
            
        return render(request, 'login.html', {'error' : error_msg}) 
      
      
      
      
      

def logout(request):
    request.session.clear()
    return redirect('Login')         



class Contact(View):
    def get(self, request):
        return render(request, "contact.html")
    
    
    
class Cart(View):
    def get(self, request):
        return render(request, "cart.html")    