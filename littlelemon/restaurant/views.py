from rest_framework import generics, viewsets
from .models import MenuItem, Booking
from .serializers import BookingSerializer, MenuItemSerializer
from rest_framework.permissions import IsAuthenticated 
from django.shortcuts import render



def home(request):
    return render(request, 'index.html')

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

