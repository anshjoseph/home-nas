
from user.models import User_Profile,User, Permission
from user_crap.models import user_crap
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,redirect,HttpResponse
from .error import data_no_found
from django import forms
# import time

class REQUEST:
    pass

class UPLOAD:
    pass


class permission:
    def __init__(self,request:REQUEST) -> None:
        self.user = request.get_request().user
    def is_block(self)->bool:
        try:
            if Permission.objects.get(user=self.user).block:
                return True
            else:
                return False
        except:
            return False
    def is_admin(self)->bool:
        try:
            if Permission.objects.get(user=self.user).admin:
                return True
            else:
                return False
        except:
            return False
    def is_normal(self)->bool:
        try:
            if Permission.objects.get(user=self.user).normal:
                return True
            else:
                return False
        except:
            return False
    def get_user_permission(self):
        return Permission.objects.get(user=self.user)


class success:
    def __init__(self,request:REQUEST,permis:Permission) -> None:
        self.request = request.get_request()
        self.permis = permis
    def success(self,message:str,req=None,upload=None,logout=None,login=None,signup=None,appstore=None)->render:
        if req != None:
            return render(self.request,"success.html",{"message":message,"admin": req,"Upload":upload,"Logout":logout,"Login":login,"Signup":signup,"Appstore":appstore})
        else:
            return render(self.request,"success.html",{"message":message,"Upload":upload,"Logout":logout,"Login":login,"Signup":signup,"Appstore":appstore})

class error:
    def __init__(self,request:REQUEST) -> None:
        self.request = request.get_request()
    def error(self,message:str)->render:
        return data_no_found(self.request,message)


class Login_logout:
    def __init__(self,request:REQUEST) -> None:
        # self.user_data = User_Profile
        self.request = request.get_request()
        return None
    def user_login(self,username:str,password:str)->bool:
        self.user = authenticate(self.request,username=username,password=password)
        if (self.user!=None):
            login(self.request,self.user)
            return True
        else:
            return False
    def ret_user(self):
        return self.user
    def user_logout(self)->bool:
        """
        login function already user authentication
        sec...
        """
        if self.request.user.is_authenticated:
            logout(self.request)
            return True
        else:
            return False
    def is_login(self)->bool:
        if self.request.user.is_authenticated:
            return True
        else:
            return False
    






class REQUEST:
    def __init__(self,request) -> None:
        self.request = request
        self.premission = permission(self)
        self.Login_logout = Login_logout(self)
        self.Error = error(self)
        self.Success = success(self,self.premission)
    def get_request(self):
        return self.request
    def set_request(self,request) -> None:
        self.request = request

    def PERMISSION(self) ->permission:
        return self.premission
    def LOGIN_LOGOUT(self) ->Login_logout:
        return self.Login_logout
    def ERROR(self) ->error:
        return self.Error
    def SUCCESS(self) ->success:
        return self.Success





