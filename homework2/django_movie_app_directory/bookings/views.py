# Various imports needed
from .models import Movie, Seat, Booking
from rest_framework import viewsets, status
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm, HistoryForm
from django.utils import timezone
from django.views.decorators.cache import never_cache
from rest_framework.response import Response
import string

def movie_lists(movies):
    """Simply gets a list of booked seats with corresponding movie and returns it as a string that looks like a list."""
    data = []

    for movie in movies:
        # Find seats based off of movie bookings
        booked_seats = Booking.objects.filter(movie=movie).values_list('seat__seat_number', flat=True)
        seats = list(booked_seats)

        # Make string that looks like list out of seats
        data_str = "[" + ", ".join(booked_seats) + "]"

        # Appends each list and its movie to the list returned
        data.append({"movie": movie.title, "booked_seats": data_str})

    return data

# Viewsets
class MovieViewSet(viewsets.ModelViewSet):
    """Movie Viewset, allows for all CRUD operations"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ViewSet):
    """Seat Viewset, allows for reading of seat info and booking info as well as booking seats"""

    # Set query set to all seats and serializer class to Seat serializer
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def list(self, request):
        """List or Read operation of API endpoint"""

        # Gets query params from URL
        seat_number = request.query_params.get('seat')
        movie_title = request.query_params.get('movie')

        # If no params simply return all movies along with their lists of seats booked
        if not seat_number and not movie_title:
            booked = movie_lists(Movie.objects.all())

            return Response(booked)

        # If no seat param but movie title param, return movie/s and booked seats for each movie under title
        elif not seat_number and movie_title:
            movies = Movie.objects.filter(title=movie_title)

            # If not valid movie, print error
            if not movies.exists():
                return Response({"error": f"Movie '{movie_title}' not found."}, status=status.HTTP_404_NOT_FOUND)

            # Get list of lists with corresponding movie
            booked = movie_lists(movies)

            return Response(booked)

        # If Only seat number in params, return error as movie is also needed
        elif not movie_title and seat_number:
            return Response({"error": "You must specify a 'movie' parameter when filtering by seat."}, 
                status=status.HTTP_400_BAD_REQUEST)

        # If both params correctly entered
        else:
            # Find the booking with the corresponding seat and movie
            seat_avail = Booking.objects.filter(seat__seat_number=seat_number,
                movie__title=movie_title).first()

            # If it exists, string becomes booked
            if seat_avail:
                if seat_avail.seat.booking_status:
                    seat_status = 'booked'
            # If not, becomes not booked
            else:
                seat_status = 'not booked'

            # Returns message concerning if the seat is taken or not
            return Response({f"Seat {seat_number} for {movie_title} is {seat_status}."})

    def create(self, request):
        """Create operation of API endpoint"""

        # Get data from request and turn it to serializer data
        serializer = SeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get objects from serializer
        movie = serializer.validated_data['movie']
        seat_number = serializer.validated_data['seat_number']
        user = serializer.validated_data['user']

        # Find all bookings from given movie
        movie_bookings = Booking.objects.filter(movie=movie)

        # Get seats that have already been taken.
        seats_taken = movie_bookings.values_list('seat__seat_number', flat=True)
        seat = None

        # Ensure the seat is in the right parameters
        if seat_number not in [f'{row}{num}' for row in string.ascii_uppercase[:8] for num in range(1, 9)]:
            raise ValidationError({"seat_number": f"Seat {seat_number} Does not exist."})
        # If the seat_number not in list, doesn't exist. We're going to create a new one and add it to the DB
        elif seat_number not in seats_taken:
            seat = Seat.objects.create(seat_number=seat_number, booking_status=True)
        # If the seat is in seats taken, send error.
        else:
            raise ValidationError({"seat_number": f"Seat {seat_number} is already booked for this movie."})

        # Create a new booking object after creation of the seat to link to movie and user
        new_booking = Booking.objects.create(movie=movie, seat=seat, user=user, booking_date=timezone.now())

        return Response({"Seat successfully booked!"}, status=status.HTTP_201_CREATED)

class BookingViewSet(viewsets.ViewSet):
    """Booking Viewset, allows for looking at the history of previous bookings and making new ones"""

    # Sets queryset to all Booking objects and serializer class
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def list(self, request):
        """Read operation of API endpoint"""

        # Gets user's name from query parameters
        user = request.query_params.get('user')

        # If there is no user parameter, return error message
        if not user:
            return Response({"error": "You must specify a 'user' parameter when looking for history."}, 
                status=status.HTTP_400_BAD_REQUEST)

        # Or else simply return list of all Booking elements
        else:
            bookings = Booking.objects.filter(user=user)
            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data)

    def create(self, request):
        """Create operation of API endpoint"""

        # Get data from request and make a BookingSerializer out of it
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get objects from data
        movie = serializer.validated_data['movie_title']
        seat_number = serializer.validated_data['seat_number']
        user = serializer.validated_data['user']

        # Get bookings from movie
        movie_bookings = Booking.objects.filter(movie=movie)

        # Get seats taken through bookings of movie
        seats_taken = movie_bookings.values_list('seat__seat_number', flat=True)
        seat = None

        # Ensure seat has proper number
        if seat_number not in [f'{row}{num}' for row in string.ascii_uppercase[:8] for num in range(1, 9)]:
            raise ValidationError({"seat_number": f"Seat {seat_number} Does not exist."})
        # If the seat_number not in list, doesn't exist. We're going to create a new one and add it to the DB
        elif seat_number not in seats_taken:
            seat = Seat.objects.create(seat_number=seat_number, booking_status=True)
        # If the seat is in seats taken, send error.
        else:
            raise ValidationError({"seat_number": f"Seat {seat_number} is already booked for this movie."})

        # Create new booking object after seat creation
        new_booking = Booking.objects.create(movie=movie, seat=seat, user=user, booking_date=timezone.now())

        return Response({"Seat successfully booked!"}, status=status.HTTP_201_CREATED)

# For HTML Rendering and UI operations

def movie_list_view(request):
    """View for rendering HTML page for movie_list with list of movies"""
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

@never_cache
def book_seat_view(request, movie_id):
    """View for rendering HTML page for book_seat with avalible seats"""

    # Get movie from given movie ID and create a bookings list of bookings under that movie only
    movie = get_object_or_404(Movie, pk=movie_id)
    bookings = Booking.objects.filter(movie_id=movie_id)

    # Get seats numbers associated with the movie from filtered bookings (dynamically generating seats)
    booked_seat_numbers = bookings.values_list('seat__seat_number', flat=True)
    # Counter for template for button grid (8 x 8 grid of seats)
    total_seats = [f'{row}{num}' for row in string.ascii_uppercase[:8] for num in range(1, 9)]

    # If the submitted form's method is POST
    if request.method == 'POST':
        # Create a BookingForm out of the submitted form (for easy error checking)
        form = BookingForm(request.POST)

        # If the form has no errors in the values that have been submitted
        if form.is_valid():
            # Get the data from the form
            user = form.cleaned_data['user']
            seat_number = form.cleaned_data['seat_number']

            seat = None

            # Stores User's name in session so it doesn't have to be shown in the URL.
            request.session['user'] = user

            # If the seat_number not in list, doesn't exist. We're going to create a new one and add it to the DB
            if seat_number not in booked_seat_numbers:
                seat = Seat.objects.create(seat_number=seat_number, booking_status=False)
            # If the seat does exist but is not currently avalible, send error back to page
            elif bookings.get(seat__seat_number=seat_number).seat.booking_status:
                form.add_error('seat_number', 'This seat just got booked. Please pick another.')

            # If a seat was chosen correctly, set its status to taken and create a new booking object.
            if (seat is not None) and (not form.errors):
                seat.booking_status = True
                seat.save()

                booking = Booking.objects.create(movie=movie, seat=seat, user=user, booking_date=timezone.now())
                # Render history page with entered User name and all booking objects
                return redirect('booking_history_with_user', user=user)

    # If method not POST, simply create a blank Form
    else:
        form = BookingForm()

    # Render in the booking page with various parameters for the template to perform logic
    return render(request, 'bookings/book_seat.html', {'form': form, 'movie': movie,'booked_seat_numbers': booked_seat_numbers,
        'total_seats': total_seats})

def booking_history_with_user_view(request, user=None):
    """View for rendering HTML page for booking_history with all booking history"""

    # If submitted form method is POST
    if request.method == 'POST':
        form = HistoryForm(request.POST)

        # Validate form and get its info
        if form.is_valid():
            user = form.cleaned_data['user']
            # Return to same view but now with user name
            return redirect('booking_history_with_user', user=user)

    # Else create a blank History Form (For posting no errors)
    else:
        form = HistoryForm()
    
    bookings = None

    # If there is a user argument
    if user:
        # Get user's bookings in reverse order
        bookings = Booking.objects.filter(user=user).order_by('booking_date').reverse()

    return render(request, 'bookings/booking_history.html', {'bookings': bookings, 'form': form, 'user': user})

def delete_booking_view(request, booking_id):
    """Not required but easier for testing, view for allowing the deletion of a booking and its seat"""

    # Get Booking from booking_id argument
    booking = get_object_or_404(Booking, id=booking_id)

    # Get seat and user associated
    seat = booking.seat
    user = booking.user

    # Deleted the booking and seat
    booking.delete()
    seat.delete()

    return redirect('booking_history_with_user', user=user)

