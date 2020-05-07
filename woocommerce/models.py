from django.db import models
from django.contrib.auth.models import User
import random, os

# Create your models here.
'''
def api_consumer_secret_generate(instance):
    chars= 'abcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(50))
    return 'cs_'+'{randomstring}',randomstr)
'''

def image_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr= ''.join((random.choice(chars)) for x in range(50))
    return 'woocommerce/'+'{userid}{randomstring}{ext}'.format(userid= instance.user.id, basename= basefilename, randomstring=randomstr, ext=file_extension)

class StoreWoo(models.Model):
    #Store Data
    name = models.CharField('Nome', max_length=50, unique=True)
    description = models.CharField('Descrição', max_length=300)
    icon = models.CharField('Ícone', max_length=10)
    color = models.CharField('Cor', max_length=7) #FF00FF
    logo = models.ImageField('Logomarca', upload_to=image_path, null=True)
    phone = models.CharField('Telefone', max_length=15)
    mobile = models.CharField('Celular', max_length=16)

    #Wordpress - Config
    wp_user = models.CharField('WP_USER', max_length=50)  
    wp_pass = models.CharField('WP_PASS', max_length=100) 

    #Wordpress - Database
    db_name = models.CharField('DB_NAME', max_length=50, unique=True)
    db_user = models.CharField('DB_USER', max_length=50) 
    db_pass = models.CharField('DP_PASS', max_length=100) 

    #Woocommerce - REST API
    api_user_id = models.IntegerField('API_USER_ID')
    api_description = models.CharField('API_DESCRIPTION', max_length=50)
    api_permissions = models.CharField('API_PERMISSIONS', max_length=15)
    api_consumer_key = models.CharField('API_CONSUMER_KEY', max_length=100)
    api_consumer_secret = models.CharField('API_CONSUMER_SECRET', max_length=100)
    api_truncate_key = models.CharField('API_TRUNCATE_KEY', max_length=20)

    #User
    user = models.ManyToManyField(User)

    #Update and Create
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'

    def __str__(self):
        return self.name