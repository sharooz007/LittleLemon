from rest_framework import generics
from .models import Menu
from .serializers import MenuItemSerializer
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
