from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .Form import OrderForm
from .models import OrderModel

# Create your views here.

def CreateOrder(request):
    form=OrderForm
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Order Sucessfully placed!!')
            return redirect('/order/')
        
    return render(request,'OrderDetails.Html',context={'data':form})

def ShowOrder(request):
    obj=OrderModel.objects.all()
    return render(request,'ShowDetails.html',context={'prform':obj})

def Home(request):
    return render(request,'home.html')

def DeleteOrder(request,f_id):
    deldata=OrderModel.objects.get(id=f_id)
    if request.method=='POST':
        con=request.POST.get('confrim')
        if con =='Yes':
            deldata.delete()
            messages.error(request,'Order Data Deleted!')
            return redirect('/show/')    
    return render(request,'confpage.html')

def UpdateOrder(request,f_id):
    updata=OrderModel.objects.get(id=f_id)
    form = OrderForm(instance=updata)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=updata)
        if form.is_valid():
            form.save()
            messages.success(request,'OrderDetails Sucessfully Updateded!')
            return redirect('/order/')
    return render(request,'OrderDetails.html',context={'data':form})



def Confpage(request):
    return render(request,'confpage.html')