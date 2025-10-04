from .models import Movie, Seat, Booking
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.exceptions import ValidationError
from django.shortcuts import render

def movie_list_view(request):
    """View for rendering HTML page for movie_list with list of movies"""
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

class MovieViewSet(viewsets.ModelViewSet):
    """Movie Viewset, allows for all CRUD operations"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    """Seat Viewset, allows for reading of seat info and booking info as well as booking seats"""
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSeat(viewsets.ModelViewSet):
    """Booking Viewset, allows for looking at the history of previous bookings and making new ones"""
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
