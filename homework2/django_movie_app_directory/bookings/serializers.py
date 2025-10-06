# Imports created models and serializers from the rest_framework
from .models import Movie, Seat, Booking
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    """Serializer for helping convert Movie model to JSON and vice versa"""
    class Meta:
        model = Movie
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    movie = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field='title', required=True, write_only=True)
    user = serializers.CharField(max_length=50, required=True, write_only=True)

    class Meta:
        model = Seat
        fields = '__all__'
        read_only_fields = ['booking_status']

class BookingSerializer(serializers.ModelSerializer):
    """Serializer for helping convert Booking model to JSON and vice versa"""
    movie_title = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field='title', required=True, write_only=True)
    seat_number = serializers.CharField(max_length=2, required=True, write_only=True)

    movie = serializers.StringRelatedField()
    seat = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['movie', 'seat', 'booking_date'] 


    