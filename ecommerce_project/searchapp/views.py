from django.shortcuts import render, redirect
from shop_app.models import Product,Category
from django.db.models import Q



# Create your views here.

def searchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
        return render(request,'search.html',{'query':query,'products':products})
