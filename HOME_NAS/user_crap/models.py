from django.db import models
from django.db.models.enums import Choices
from django.db.models.signals import post_delete
from django.dispatch import receiver
from HOME_NAS import settings
import os
bs = settings.BASE_DIR

# Create your models here.
class user_crap(models.Model):
    choices = [("app","app"),("pdf","pdf"),("video","video"),("doc","doc"),("compress_file","compress_file"),("image","image"),("music","music")]
    #----------------------------------
    user = models.CharField(max_length=40)
    title = models.CharField(max_length=90)
    data = models.FileField()
    decs = models.TextField(max_length=400)
    type_data = models.CharField(max_length=20,choices=choices)
    def __str__(self):
        return self.title

@receiver(post_delete,sender=user_crap)
def del_file(**kargs):
    file = str(kargs.get('instance').data)
    print(f"{bs}\media\{file}")
    os.remove(f"{bs}\media\{file}")

# class addition_file(models.Model):
#     uc = models.OneToOneField(user_crap,on_delete=models.CASCADE)
#     data = models.FileField(blank=True,null=True,upload_to='user_crap_extra/')
# @receiver(post_delete,sender=addition_file)
# def del_File(**kargs):
#     file = str(kargs.get('instance').data).replace('/','\\')
#     os.remove(f"{bs}\media\{file}")
