from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import Menuserializer,Bookingserializer,Userserializer
from django.contrib.auth.models import User
from .models import Menu,Booking
# Create your views here.
def index(request):
    return render(request,"index.html",{})

class Menuitemview(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=Menuserializer
    permission_classes=[IsAuthenticated]
class singlemenuitemview(generics.RetrieveDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=Menuserializer
class Bookingviewset(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=Bookingserializer
    permission_classes=[IsAuthenticated]
class Userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=Userserializer
    permission_classes=[IsAuthenticated]