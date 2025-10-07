# Various needed imports
from rest_framework.test import APITestCase
from django.test import TestCase
from datetime import datetime, timedelta
from bookings.models import Movie, Seat, Booking
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from django.utils.dateparse import parse_datetime
from django.core.exceptions import ValidationError

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

    def test_seat_creation(self):
        """Ensures after creation fields match and object is of seat type"""
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertEqual(self.seat.booking_status, True)
        self.assertTrue(isinstance(self.seat, Seat))

    def test_seat_str(self):
        """Ensures __str__ returns movie title"""
        self.assertEqual(str(self.seat), "A1")

    def test_seat_number(self):
        """Ensures that validation error occurs with seat input outside of range using clean method of model"""
        seat = Seat(seat_number="Z9", booking_status=False)
        with self.assertRaises(ValidationError) as context:
            seat.full_clean()  # This should trigger the clean() method

class BookingModelTests(TestCase):
    """Class for testing all aspects of the Booking Model"""
    testDate = timezone.now() - timedelta(days=10)

    # Sets up booking to be tested
    def setUp(self):
        self.movie = Movie.objects.create(title="Avatar", description="Sci-Fi", 
            release_date = self.testDate, duration = timedelta(hours=2, minutes=15))
        self.seat = Seat.objects.create(seat_number="A1", booking_status=True)
        self.booking = Booking.objects.create(movie=self.movie, seat=self.seat, user='Test', booking_date=self.testDate)

    def test_seat_creation(self):
        """Ensures after creation fields match and object is of booking type"""
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, 'Test')
        self.assertEqual(self.booking.booking_date, self.testDate)
        self.assertTrue(isinstance(self.booking, Booking))

class MovieListSingleTest(APITestCase):
    """Ensures that a list is properly returned from the api endpoint /api/movies"""
    testDate = timezone.now() - timedelta(days=10)

    # Sets up one movie to be tested
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

class MovieCRUDTests(APITestCase):
    """Test CRUD operations for the /api/movies endpoint."""

    def setUp(self):
        """Sets up various objects for Testing"""
        self.test_date = timezone.now() - timedelta(days=10)
        self.movie = Movie.objects.create(title="Avatar", description="Sci-Fi", release_date=self.test_date,
            duration=timedelta(hours=2, minutes=28))

        self.list_url = reverse('movie-list')
        self.detail_url = reverse('movie-detail', args=[self.movie.id])

    # Create
    def test_create_movie(self):
        """Ensure a new movie can be created."""
        data = {"title": "Titanic", "description": "Big Iceberg", "release_date": str(timezone.now().date()),
            "duration": "02:15:00"}

        # get the response of API Post call
        response = self.client.post(self.list_url, data, format='json')

        # Ensure proper response code, that there are now tow movies in DB, and that the one with title Titanic
        # has proper description
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(Movie.objects.get(title="Titanic").description, "Big Iceberg")

    # Read list
    def test_list_movies(self):
        """Ensure the API returns a list of movies."""
        response = self.client.get(self.list_url)

        # Ensure status code and that movie in list
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertIn("Avatar", [m["title"] for m in response.data])

    # Read singular
    def test_retrieve_single_movie(self):
        """Ensure a single movie can be retrieved by ID."""
        response = self.client.get(self.detail_url)

        # Ensure you can grab a singular movie
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Avatar")
        self.assertEqual(response.data["description"], "Sci-Fi")

    # Update
    def test_update_movie(self):
        """Ensure a movie can be updated."""
        updated_data = {"title": "Avatar Updated", "description": "Sci-Fi",
            "release_date": str(self.test_date.date()), "duration": "02:28:00"}

        response = self.client.put(self.detail_url, updated_data, format='json')

        # Make sure data was updated in DB
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Avatar Updated")

    # Delete
    def test_delete_movie(self):
        """Ensure a movie can be deleted."""
        response = self.client.delete(self.detail_url)

        # Ensure Delete code and that the object doesn't exist after it has been deleted.
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())


class SeatEndpointTests(APITestCase):
    """Tests various cases for endpoint /api/seat"""
    testDate = timezone.now() - timedelta(days=10)

    # Sets up movie to be tested
    def setUp(self):
        self.movie = Movie.objects.create(title="Avatar", description="Sci-Fi", 
            release_date = self.testDate, duration = timedelta(hours=2, minutes=15))
        self.seat = Seat.objects.create(seat_number="A1", booking_status=True)
        self.url = reverse('seat-list')

    def test_list_seats(self):
        """Ensure the seat endpoint returns seats"""

        # With query parameters, makes sure seat is properly returned
        response = self.client.get(self.url + '?movie=Avatar&seat=A1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"Seat A1 for Avatar is not booked."})

    def test_book_seat(self):
        """Test booking a seat"""

        # Sends Json data and asserts its response provides a creation code and that its return is a success string.
        data = {"movie": self.movie.title, "seat_number": self.seat.seat_number, "user": "John"}
        response = self.client.post(self.url, data, format='json')

        # Ensures that creation code, success string, and that the object exists in the DB
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"Seat successfully booked!"})
        self.assertTrue(Booking.objects.filter(user="John", movie=self.movie).exists())

    def test_double_booking_rejected(self):
        """Ensure booking a taken seat fails"""

        # Attempts to send info to API to book, but will fail because seat already taken
        Booking.objects.create(movie=self.movie, seat=self.seat, user="Bob",booking_date=timezone.now())
        data = {"seat_number": "A1", "user": "Charlie", "movie": "Matrix"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class BookingEndpointTests(APITestCase):
    """Tests for the Booking api endpoint /api/bookings/"""
    def setUp(self):
        """Sets up objects to test various Booking API functions"""
        self.testDate = timezone.now() - timedelta(days=10)
        self.movie = Movie.objects.create(title="Avatar", description="Sci-Fi", release_date=self.testDate,
            duration=timedelta(hours=2, minutes=15))

        self.booking_url = reverse('booking-list')
        self.user = "John"

    def test_create_booking_success(self):
        """Ensure a booking can be successfully created"""

        # Creates mock data
        data = {"movie_title": self.movie.title, "seat_number": "A1", "user": self.user}

        response = self.client.post(self.booking_url, data, format='json')

        # Ensures creation code, return message, and that the booking exists
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"Seat successfully booked!"})
        self.assertTrue(Booking.objects.filter(user=self.user, movie=self.movie).exists())

    def test_double_booking_rejected(self):
        """Ensure booking the same seat twice for the same movie fails"""
        # Create a booking in the DB
        Booking.objects.create(movie=self.movie, seat=Seat.objects.create(seat_number="A1", booking_status=True),
            user=self.user, booking_date=timezone.now()
        )

        # Try to book same seat
        data = {"movie_title": self.movie.title, "seat_number": "A1", "user": "Jane"}

        response = self.client.post(self.booking_url, data, format='json')

        # Assert Bad request and that already booked appears in response string.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("already booked", str(response.data))

    def test_list_user_bookings(self):
        """Ensure listing a user's bookings works"""

        # Create a seat and booking object from said seat
        seat = Seat.objects.create(seat_number="B2", booking_status=True)
        Booking.objects.create(movie=self.movie, seat=seat, user=self.user, booking_date=timezone.now())

        # Get response by entering query parameter for user, should be list of bookings
        url = f"{self.booking_url}?user={self.user}"
        response = self.client.get(url, format='json')

        # Ensure that request success code, length of returned list is 1, and that Avatar and B2 appear in the one response.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['movie'], "Avatar")
        self.assertEqual(response.data[0]['seat'], "B2")




