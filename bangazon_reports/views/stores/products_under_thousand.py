from django.shortcuts import render
from django.db import connection
from django.views import View
from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework import status
from bangazon_api.models import Store
from django.contrib.auth.models import User
from rest_framework.response import Response
from bangazon_api.models import product

from bangazon_api.models.product import Product
class ProductUnderThousand(View):
    def get(self, request):
        
        stores_products = []
        try:
            products = Product.objects.filter(price__lte=1000).order_by("price")
            
            data = ProductSerializer(products, many=True, context={'request': request})
            stores_products = data.data
            template = 'stores_products_over_thousand.html'
            context = {'products': stores_products, 'title':'Products Under $1000'}
            return render(request, template, context)
        except:
            pass



class StoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
class StoreSerializer(serializers.ModelSerializer):
    seller = StoreUserSerializer()
    
    class Meta:
        model = Store
        fields = ('id', 'name', 'description', 'seller')

class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'price','store')