from rest_framework import response, status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.core.management import call_command
from django.contrib.auth.models import User
from datetime import date, datetime
from bangazon_api.models import Order, Product, PaymentType


class OrderTests(APITestCase):
    def setUp(self):
        """
        Seed the database
        """
        call_command('seed_db', user_count=3)
        self.user1 = User.objects.filter(store=None).first()
        self.token = Token.objects.get(user=self.user1)

        self.user2 = User.objects.filter(store=None).last()
        product = Product.objects.get(pk=1)

        self.order1 = Order.objects.create(
            user=self.user1
        )

        self.order1.products.add(product)

        self.order2 = Order.objects.create(
            user=self.user2
        )

        self.order2.products.add(product)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}')
        payment_method = PaymentType()
        payment_method.acct_number = "12345"
        payment_method.merchant_name = "blues Clues"
        payment_method.customer = self.user2
        payment_method.save() 


    def test_list_orders(self):
        """The orders list should return a list of orders for the logged in user"""
        response = self.client.get('/api/orders')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_delete_order(self):
        response = self.client.delete(f'/api/orders/{self.order1.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_complete_order(self):
        """This test checks if a order gets completed"""
        order = Order()
        order.user = User.objects.get(pk=1)
        order.save()
        url = f'/api/orders/{order.id}/complete'
        new_order = {
            
            "paymentTypeId": 1
        }
        response = self.client.put(url, new_order, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_new_line_not_added_to_order(self):
        self.order1.completed_on = datetime.now()
        self.order1.save()
        url = f"/api/products/1/add_to_order"
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.order2.completed_on = datetime.now()
        self.order2.save()
        
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data["order_id"], self.order1.id)
        self.assertNotEqual(response.data["order_id"], self.order2.id)


