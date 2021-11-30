from django.shortcuts import render
from django.db import connection
from django.views import View
from rest_framework.viewsets import ViewSet

from bangazon_api.models import Order
from django.db.models import Q
from bangazon_api.serializers import OrderSerializer
class IncompletedOrders(View):
    def get(self, request):
        
        
        try:
            orders = Order.objects.filter(completed_on=None)
            
            
            
            template = 'completed_orders.html'
            context = {'orders': orders, 'title':'Incomplete Orders'}
            return render(request, template, context)
        except:
            pass



