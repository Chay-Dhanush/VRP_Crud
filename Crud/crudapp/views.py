import json
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .serializers import getserilaze
from rest_framework import status
from .Form import OrderForm
from .models import OrderModel
from rest_framework.decorators import api_view

# Create your views here.

def CreateOrder(request):
    form=OrderForm
    if request.method=='POST':
        form=OrderForm(request.POST)
        # data = json.loads(request.body)
        # form = OrderForm(data)
        print(form)
        print(request)
        if form.is_valid():
            form.save()
            messages.success(request,'Order Sucessfully placed!!')
            return redirect('/order/')
        
    return render(request,'OrderDetails.Html',context={'data':form})


# @api_view(["GET"])
def ShowOrder(request):
    obj=OrderModel.objects.all()
    # serialize=getserilaze(obj,many=True)
    # return Response(serialize.data)
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

@api_view(["GET"])
def serialize(request):
    if request.method=='GET':
        model=OrderModel.objects.all()
        serialize=getserilaze(model,many=True)
        return Response(serialize.data)
    # elif request.method=='POST':
    #     return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def gserialize(request):
    if request.method=='POST':
        serialize=getserilaze(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def Pserialize(request,f_id):
    try:
        model=OrderModel.objects.get(id=f_id)
        if request.method=='PUT':
            serialize=getserilaze(model,data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def Delete(request,f_id):
    try:
        model=OrderModel.objects.get(id=f_id)
        if request.method=='DELETE':
            model.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except OrderModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)