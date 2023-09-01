from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name 
        
    
    
class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default=" ", null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    
    
    # methods for product collection
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category = category_id)   
        else:
            return Products.get_all_products()
        
    def get_product_details(self):
        return {
            'name': self.name,
            'description': self.description,
            'image': self.image.url ,  # Make sure to adjust this based on your image field
            'price': self.price,
        }        
        
        




class Customer(models.Model):
    cname = models.CharField(max_length=100)
    cemail = models.EmailField()
    phone = models.IntegerField(10)
    password = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.cname 
    
    
    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(cemail):
        try:
            return Customer.objects.get(cemail=cemail) 
        except Customer.DoesNotExist:
            return None       
        
    def isExistEmail(self):
        if Customer.objects.filter(cemail = self.cemail):
            return True
            
        else:
            return False    
    
