from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HotelSerializer,ManagerSerializer,GuestSerializer,RoomSerializer,BookingSerializer
from .models import Hotel,Manager,Guest,Room,Booking
from rest_framework import status
from rest_framework import generics


# @api_view (['GET','PUT','POST','DELETE',])
# def api_view_list_hotels(request):
#     list_hotels = Hotel.objects.all()
#     if request.method == 'GET':
#         serializers = HotelSerializer(list_hotels, many=True)
#         return Response(serializers.data)
#
#
# @api_view (['GET'])
# def api_view_hotel_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             hotel = Hotel.objects.get(id = pk)
#         except Hotel.DoesNotExist:
#             return Response(status.HTTP_404_NOT_FOUND)
#         serializers = HotelSerializer(hotel)
#     return Response(serializers.data)
#
# @api_view(['PUT'])
# def api_update_hotel(request, pk):
#     try:
#         hotel = Hotel.objects.get(id=pk)
#     except Hotel.DoesNotExist:
#         return Response(status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         serializer = HotelSerializer(hotel,data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data["success"] = "Update Successful"
#         else:
#             data["failure"] = "Update failed"
#             return Response(data, status=status.HTTP_200_OK)
#
# @api_view(['POST'])
# def api_post_hotel(request):
#     if request.method == 'POST':
#         serializer = HotelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['DELETE'])
# def api_delete_hotel(request, pk):
#     try:
#         hotel =Hotel.objects.get(id=pk)
#     except Hotel.DoesNotExist:
#         return Response(status.HTTP_404_NOT_FOUND)
#     if request.method == 'DELETE':
#         hotel.delete()
#         data={}
#         data["success"]="Deleted Successfully"
#         return Response(data,status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# def api_view_list_managers(request):
#     list_managers= Manager.objects.all()
#     if request.method == 'GET':
#         serializers = ManagerSerializer(list_managers, many = True)
#         return Response(serializers.data)
#
# @api_view(['GET'])
# def api_view_list_guests(request):
#     list_guest=Guest.objects.all()
#     if request.method == 'GET':
#         serializers = GuestSerializer(list_guest, many = True)
#         return  Response(serializers.data)
#
# @api_view (['GET'])
# def api_view_list_rooms(request):
#     list_room=Room.objects.all()
#     if request.method == 'GET':
#         serializers = RoomSerializer(list_room, many = True)
#         return Response(serializers.data)
#
#
#
# @api_view (['GET'])
# def api_view_list_bookings(request):
#     list_booking=Booking.objects.all()
#     if request.method == 'GET':
#         serializers = BookingSerializer(list_booking, many = True)
#         return Response(serializers.data)


class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelRetrieve(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer



















































# from rest_framework import viewsets
# from .serializers import HotelSerializer,ManagerSerializer,GuestSerializer,RoomSerializer,BookingSerializer
# from .models import Hotel,Manager,Guest,Room,Booking
#
#
# class HotelViewset(viewsets.ModelViewSet):
#     serializer_class = HotelSerializer
#     queryset = Hotel.objects.all()
#
# class ManagerViewset(viewsets.ModelViewSet):
#     serializer_class = ManagerSerializer
#     queryset = Manager.objects.all()
#
# class GuestViewset(viewsets.ModelViewSet):
#     serializer_class = GuestSerializer
#     queryset = Guest.objects.all()
#
# class RoomViewset(viewsets.ModelViewSet):
#     serializer_class = RoomSerializer
#     queryset = Room.objects.all()
#
# class BookingViewset(viewsets.ModelViewSet):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()


# Create your views here.
