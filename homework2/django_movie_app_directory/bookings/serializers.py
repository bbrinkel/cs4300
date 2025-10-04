# Imports created models and serializers from the rest_framework
from .models import Movie, Seat, Booking
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    """Serializer for helping convert Movie model to JSON and vice versa"""
    class Meta:
        model = Movie
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    """Serializer for helping convert Seat model to JSON and vice versa"""
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """Serializer for helping convert Booking model to JSON and vice versa"""
    class Meta:
        model = Booking
        fields = '__all__'

    