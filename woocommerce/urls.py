from django.urls import path
from . import views

app_name = 'woocommerce'

urlpatterns = [
    path('', views.list_stores, name='list_stores'),
]
