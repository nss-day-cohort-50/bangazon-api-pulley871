from django.urls import path
from .views import ProductOverThousand, ProductUnderThousand, CompletedOrders
urlpatterns = [
    path('reports/storeproductsoverthousand', ProductOverThousand.as_view()),
    path('reports/storeproductsunderthousand', ProductUnderThousand.as_view()),
    path('reports/completedorders', CompletedOrders.as_view())
]
