from django.urls import path, include

from booking import views

urlpatterns = [
    path('booking-list/', views.BookingViewSet.as_view({ 'get': 'list'})),
    path('booking/<int:id>', views.BookingDetail.as_view({'get': 'get'})),
]
