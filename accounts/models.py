from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from uuid import uuid4
from datetime import datetime
import os
import random


# Create your models here.

def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(50))
    #return 'images/userphotos/{userid}/{basename}{randomstring}{ext}'.format(userid= instance.user.id, basename= basefilename, randomstring= randomstr, ext= file_extension)
    return 'accounts/'+'{userid}{randomstring}{ext}'.format(userid= instance.user.id, basename= basefilename, randomstring=randomstr, ext=file_extension)


class UserProfile(models.Model):
    upload_dir = uuid4().hex
    #upload_dir += datetime.datetime.now()
    #photo = models.ImageField('Foto', upload_to=upload_dir)
    photo = models.ImageField('Foto', upload_to=photo_path, null=True)
    cell_phone = models.CharField('Celular', max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Perfil do usuário'
        verbose_name_plural = 'Perfis dos usuários'

    def __str__(self):
        return self.user.username