from django.shortcuts import render
from django.db import connection
from django.views import View
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from bangazon_api.models import Order
from django.db.models import Q
from bangazon_api.models.favorite import Favorite
from bangazon_api.serializers import OrderSerializer
class CustomerFavorites(View):
    def get(self, request):
        
        completed_orders = []
        try:
            customers = User.objects.all()
            for customer in customers:
                customer.favorite_stores = customer.favorites.all()
            
            
            template = 'customers_favorite_stores.html'
            context = {'customers': customers, 'title':'Customer Favorites'}
            return render(request, template, context)
        except:
            pass



