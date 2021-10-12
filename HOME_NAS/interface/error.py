from django.shortcuts import render

def data_no_found(request,message):
    return render(request,"error/nodata.html",{"message":message})