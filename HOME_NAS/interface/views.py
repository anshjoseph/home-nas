from interface.error import data_no_found
from django.shortcuts import render,redirect,HttpResponse
from user.models import User_Profile,User, Permission
from user_crap.models import user_crap
from .error import data_no_found
from .utily import REQUEST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import HOME_PAGE_IMAGE,HOME_PAGE_ARTICALSE
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse




# Create your views here



#1
def home(request):
    # return HttpResponse("hello world")
    req = REQUEST(request)
    imgs = list(HOME_PAGE_IMAGE.objects.all())
    articles = list(HOME_PAGE_ARTICALSE.objects.all())
    img = None
    try:
        img = imgs[0]
        imgs = imgs[1:]
    except:
        imgs = None
        img = None
    return render(request,"home.html",{"pg_no":1,"imgs":imgs,"img":img,"toggle":0,"articles":articles})


"""____________"""
#2 comes under appstore
def upload(request):
    req = REQUEST(request)
    objs = list()
    for oj in user_crap.objects.all():
        objs.append(oj.title)
    objs = set(objs)
    if req.LOGIN_LOGOUT().is_login():
        # if request.method == "POST":
        #     user = request.POST.get("user")
        #     title = request.POST.get("title")
        #     file = request.FILES.get("file")
        #     decs = request.POST.get("decs")
        #     data_type = request.POST.get("data_type")
        #     if user != None and title != None and file != None and decs != None and data_type != None:
        #         try:
        #             print(type(file))
        #             user_crap.objects.create(user=user,title=title,data=file,decs=decs,type_data=data_type)
        #             return req.SUCCESS().success(f"your data is uploaded file name:-{file} and title:-{title}",req=None,upload=True,appstore=True)
        #         except Exception as e:
        #             print(e)
        #             return req.ERROR().error("Some thimg went wrong")
        #         pass
        #     else:
        #         return req.ERROR().error("Some feilds are missing")
        #     # print(user,title,file,decs)
        if request.is_ajax():
            user = request.POST.get("user")
            title = request.POST.get("title")
            file = request.FILES.get("file")
            decs = request.POST.get("decs")
            data_type = request.POST.get("data_type")
            if user != None and title != None and file != None and decs != None and data_type != None:
                try:
                    # print(type(file))
                    user_crap.objects.create(user=user,title=title,data=file,decs=decs,type_data=data_type)
                    return req.SUCCESS().success(f"your data is uploaded file name:-{file} and title:-{title}",req=None,upload=True,appstore=True)
                except Exception as e:
                    print(e)
                    return req.ERROR().error("Some thimg went wrong")
                pass
            else:
                return req.ERROR().error("Some feilds are missing")
            # print(user,title,file,decs)
    else:
        return req.ERROR().error("you have to login first")
    return render(request,"upload.html",{"pg_no":2,"user":str(request.user),"objs":objs})
#2
def appstore(request):
    req = REQUEST(request)
    flag = 0
    data_type = ["app","music","pdf","doc","video","compress_file","image"]
    objs = list(user_crap.objects.all())[-100:]
    items = list()
    for oj in user_crap.objects.all():
        items.append(oj.title)
    items = set(items)
    items = list(items)
    items.extend(data_type)
    
    if request.method == "POST":
        item = request.POST.get("search")
        copy = item
        if copy.lower() in data_type:
            temp = user_crap.objects.filter(type_data__contains=item)
        else:
            temp = user_crap.objects.filter(title__contains=item)
        objs = list(temp)
        try:
            objs[0]
            print(" ")
        except:
            flag += 1
        
    if flag != 0:
        return req.ERROR().error("No data found")

    return render(request,"appstore.html",{"pg_no":2,"objs":objs,"items":items})

#2
@xframe_options_sameorigin
def show_data(request):
    req = REQUEST(request)
    if request.method == "POST":
        ID = request.POST.get("id")
        
        if ID != None:
            data = user_crap.objects.get(id = ID)
            
            return render(request,"ysdfgjdgsj.html",{"pg_no":2,"data":data})
    else:
        return req.ERROR().error("This page is not ment to use in this way")
"""____________"""

#3
def signup(request):
    req = REQUEST(request)
    if req.LOGIN_LOGOUT().is_login():
        return req.ERROR().error("You are already login in for sign up you have to logout")

    if request.method == "POST":
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,"signup.html",{"pg_no":3,"form":form})
# 2
# audio
# @csrf_exempt
# def audio(request):
#     if request.method == "POST":
#         obj_id = request.POST.get('obj_id')
#     return HttpResponse("audio")

#4
def login(request):
    req = REQUEST(request)
    if req.LOGIN_LOGOUT().is_login():
        return redirect("home")


    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if len(username) == 0 or len(password) == 0:
            # print("hello")
            return req.ERROR().error("username or password is empty")
        else:
            if(req.LOGIN_LOGOUT().user_login(username,password)):
               user = req.LOGIN_LOGOUT().ret_user()
               return req.SUCCESS().success("you are login",user.is_superuser)
            else:
                return req.ERROR().error("Login not successful")
        
    return render(request,"login.html",{"pg_no":4})



def logout(request):
    req = REQUEST(request)
    if req.LOGIN_LOGOUT().user_logout():
        return req.SUCCESS().success("you are logout")
    else:
        return req.ERROR().error("Your are not login")

