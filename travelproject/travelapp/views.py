from django.http import HttpResponse
from django.shortcuts import render
from  .models import Place,News


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    news=News.objects.all()
    return render(request, 'index.html',{'result':obj,'n_reprt':news})




# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
#

