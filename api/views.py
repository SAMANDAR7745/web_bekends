from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.serializers import *
from main.models import *
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
import django_filters
from rest_framework import filters
from django.shortcuts import render

#
# class CategoryCreateListView(APIView):
#     def get(self, request: Request):
#         products = Category.objects.all().order_by('-id')
#         serializer = CategorySerializer(products, many=True)
#         return Response(data={"category": serializer.data})
#
#
# class CategoryRetrieveUpdateDestroyAPIView(APIView):
#     permission_classes = (IsAdminUser,)
#
#     def get(self, request, pk):
#         product = get_object_or_404(Category, pk=pk)
#         serializer = CategorySerializer(product)
#         return Response(data=serializer.data)
#
#     def put(self, request, pk):
#         product = get_object_or_404(Category, pk=pk)
#         data = request.data
#         serializer = CategorySerializer(instance=product, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     def delete(self, request, pk):
#         Category.objects.filter(id=pk).delete()
#         return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FoodCreateListView(APIView):
    def get(self, request: Request):
        food = Food.objects.all().order_by('-id')
        serializer = FoodSerializer(food, many=True)
        return Response(data={"food": serializer.data})


class FoodRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        serializer = FoodSerializer(food)
        return Response(data=serializer.data)

    def put(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        data = request.data
        serializer = FoodSerializer(instance=food, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self, request, pk):
        Food.objects.filter(id=pk).delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class OrderCreateListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["is_paid", 'shipping', "client"]

    # def get_queryset(self):
    #     return Order.objects.filter(is_paid=False)


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    location_field = 'pk'


class OrderItemCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    location_field = 'pk'


class ClientCreateListView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

    # def get_queryset(self):
    #     queryset = Client.objects.all()
    #     name = self.request.query_params.get('name')
    #     if name is not None:
    #         return Client.objects.filter(full_name__icontains=name)
    #     return queryset


class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    location_field = 'pk'



