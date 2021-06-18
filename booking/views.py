from django.http import Http404
from django.shortcuts import render
from rest_framework import pagination, serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import pagination
from django_filters import rest_framework as filters
from .models import Bookings
from .serializers import BookingSerializer

class BookingFilter(filters.FilterSet):

    class Meta:
        model = Bookings
        fields = {
            'pod_name': ['icontains'],
            'price': ['exact'],
            'status': ['exact'],
            'booking_date': ['iexact', 'lte', 'gte'],
        }

class CostumPagination(pagination.PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    pagination_class = CostumPagination
    filterset_class = BookingFilter

    def get_queryset(self):
        return Bookings.objects.order_by('booking_date')

class BookingDetail(ModelViewSet):
    def get_object(self, id):
        try:
            return Bookings.objects.get(pk=id)
        except Bookings.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        booking = self.get_object(id)
        print(booking)
        serializers = BookingSerializer(booking)
        return Response(serializers.data)



