from django.shortcuts import render

from .models import student

def fun1(request):
    return render(request,'display.html')


def fun2(request):
    if request.method=="POST":
        a=request.POST['us']
        b=request.POST['pa']
        sd=student(name=a,password=b)
        sd.save()
    return render(request,'display.html')

