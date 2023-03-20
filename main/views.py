from django.shortcuts import render
from rest_framework.views import APIView

class PricePlan(APIView):
    def get(self, request):
        return render(request, "home_page/home.html")
    
class ABOUT(APIView):
    def get(self, request):
        return render(request, "home_page/about.html")