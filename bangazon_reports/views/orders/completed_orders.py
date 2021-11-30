from django.shortcuts import render
from django.db import connection
from django.views import View
from rest_framework.viewsets import ViewSet

from bangazon_api.models import Order
from django.db.models import Q
from bangazon_api.serializers import OrderSerializer
class CompletedOrders(View):
    def get(self, request):
        
        completed_orders = []
        try:
            orders = Order.objects.filter(~Q(completed_on=None))
            
            
            
            template = 'completed_orders.html'
            context = {'orders': orders, 'title':'Completed Orders'}
            return render(request, template, context)
        except:
            pass



