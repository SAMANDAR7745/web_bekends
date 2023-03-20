from django.urls import path
from .views import PricePlan, ABOUT

urlpatterns = [
    path('', PricePlan.as_view(), name='h'),
    path('about/', ABOUT.as_view(), name="about")

]