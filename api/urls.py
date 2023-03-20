from django.urls import path, re_path
from .views import *
from .auth import UserViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r"users", UserViewSet, basename="user")
# router.register(r"cats", CategoryViewSet, basename="cats")
# user_list = UserViewSet.as_view({"get": "list", "post": "create"})
# user_detail = UserViewSet.as_view({'get': "retrieve", 'put': "update", "delete": "destroy"})

urlpatterns = [
    # path('cats/', CategoryCreateListView.as_view(), name="cats"),
    # path('cats/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="cats_detail "),
    path('food/', FoodCreateListView.as_view(), name=''),
    path('food/<int:pk>/', FoodRetrieveUpdateDestroyAPIView.as_view(), name='food_detail'),
    path('order/', OrderCreateListView.as_view(), name='order'),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order_detail'),
    path('order_items/', OrderItemCreateListView.as_view(), name='order_items'),
    path('order_items/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='order_items_detail'),
    path('client', ClientCreateListView.as_view(), name='client'),
    path('client/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client_detail'),
    # path('users/', user_list, name="user_list"),
    # path('users/<int:pk>/', user_detail, name="user_detail")

]
# ] + router.urls
