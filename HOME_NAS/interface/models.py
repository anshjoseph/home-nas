from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from HOME_NAS import settings
import os
bs = settings.BASE_DIR

# Create your models here.
class HOME_PAGE_IMAGE(models.Model):
    image = models.ImageField(upload_to='home_img/')
@receiver(post_delete,sender=HOME_PAGE_IMAGE)
def del_file1(**kargs):
    file = str(kargs.get('instance').image).replace('/','\\')
    os.remove(f"{bs}\media\{file}")
    
class HOME_PAGE_ARTICALSE(models.Model):
    title = models.TextField(max_length=250)
    image = models.ImageField(upload_to='home_articals_img/')
    decs = models.TextField(max_length=400)
    def __str__(self) -> str:
        return self.title
@receiver(post_delete,sender=HOME_PAGE_ARTICALSE)
def del_file2(**kargs):
    file = str(kargs.get('instance').image).replace('/','\\')
    os.remove(f"{bs}\media\{file}")