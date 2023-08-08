from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    
    
    
    def __str__(self):
        return self.name 
        
    
    
class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    product_id = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default=" ", null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    
    
    # methods for product collection
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
