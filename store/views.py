from django.shortcuts import render, HttpResponse
from .models import Products

# Create your views here.
def index(request):
    prds = Products.get_all_products()
    return render(request, "index.html", {'products': prds})
