from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
user = settings.AUTH_USER_MODEL
# Create your models here.
class User_Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200,default="not defined")
    def __str__(self):
        return self.user_name
@receiver(post_save,sender=user)
def set_username(**kargs):
    username = kargs.get('instance')
    if len(User_Profile.objects.filter(user_name=username)) == 0:
        User_Profile(user=username,user_name=str(username)).save()

class Permission(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200,default="not defined")
    admin = models.BooleanField(default=False)
    normal = models.BooleanField(default=True)
    block = models.BooleanField(default=False)
    def __str__(self):
        return self.user_name
@receiver(post_save,sender=user)
def set_username_per(**kargs):
    username = kargs.get('instance')
    if len(Permission.objects.filter(user_name=username)) == 0:
        Permission(user=username,user_name=str(username)).save()