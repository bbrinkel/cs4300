from rest_framework.test import APITestCase
from django.test import TestCase
from datetime import datetime, timedelta
from bookings.models import Movie, Seat, Booking
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from django.utils.dateparse import parse_datetime

class MovieModelTests(TestCase):
    """Class for testing all aspects of the Movie Model"""
    testDate = timezone.now() - timedelta(days=10)

    # Sets up movie to be tested
    def setUp(self):
        self.movie = Movie.objects.create(title="Avatar", description="Sci-Fi", 
            release_date = self.testDate, duration = timedelta(hours=2, minutes=15))

    # Ensures after creation fields match and object is of movie type
    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Avatar")
        self.assertEqual(self.movie.description, "Sci-Fi")
        self.assertEqual(self.movie.release_date, self.testDate)
        self.assertEqual(self.movie.duration, timedelta(hours=2, minutes=15))
        self.assertTrue(isinstance(self.movie, Movie))

    # Ensures __str__ returns movie title
    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Avatar")

class SeatModelTests(TestCase):
    """Class for testing all aspects of the Seat Model"""

    # Sets up seat to be tested
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A1", booking_status=True)

    # Ensures after creation fields match and object is of seat type
    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertEqual(self.seat.booking_status, True)
        self.assertTrue(isinstance(self.seat, Seat))

    # Ensures __str__ returns movie title
    def test_seat_str(self):
        self.assertEqual(str(self.seat), "A1")

class BookingModelTests(TestCase):
    """Class for testing all aspects of the Booking Model"""
    testDate = timezone.now() - timedelta(days=10)

    # Sets up booking to be tested
    def setUp(self):
        self.movie = Movie.objects.create(title="Avatar", description="Sci-Fi", 
            release_date = self.testDate, duration = timedelta(hours=2, minutes=15))
        self.seat = Seat.objects.create(seat_number="A1", booking_status=True)
        self.booking = Booking.objects.create(movie=self.movie, seat=self.seat, user='Test', booking_date=self.testDate)

     # Ensures after creation fields match and object is of booking type
    def test_seat_creation(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, 'Test')
        self.assertEqual(self.booking.booking_date, self.testDate)
        self.assertTrue(isinstance(self.booking, Booking))

class MovieListSingleTest(APITestCase):
    """Ensures that a list is properly returned from the api endpoint /api/movies"""
    testDate = timezone.now() - timedelta(days=10)

    # Setups up one movie to be tested
    def setUp(self):
        self.movie = Movie.objects.create(title="Avatar", description="Sci-Fi", 
            release_date = self.testDate, duration = timedelta(hours=2, minutes=15))

        # router auto-names endpoint as 'movie-list'
        self.url = reverse('movie-list')  

    # Ensure HTTP response has correct fields
    def test_list_contains_single_movie(self):
        """Ensure API returns exactly one movie"""
        response = self.client.get(self.url)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that only one movie is returned
        self.assertEqual(len(response.data), 1)

        # Check the correct movie attributes
        api_date = parse_datetime(response.data[0]['release_date'])
        self.assertEqual(response.data[0]['title'], "Avatar")
        self.assertEqual(response.data[0]['description'], "Sci-Fi")
        self.assertEqual(api_date, self.testDate)
        self.assertEqual(response.data[0]['duration'], "02:15:00")

class SeatEndpointTests(APITestCase):
    testDate =