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
    data = []

    for movie in movies:
        booked_seats = Booking.objects.filter(movie=movie).values_list('seat__seat_number', flat=True)
        seats = list(booked_seats)

        data_str = "[" + ", ".join(booked_seats) + "]"

        data.append({"movie": movie.title, "booked_seats": data_str})

    return data

# Viewsets
class MovieViewSet(viewsets.ModelViewSet):
    """Movie Viewset, allows for all CRUD operations"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ViewSet):
    """Seat Viewset, allows for reading of seat info and booking info as well as booking seats"""

    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def list(self, request):
        seat_number = request.query_params.get('seat')
        movie_title = request.query_params.get('movie')

        if not seat_number and not movie_title:
            booked = movie_lists(Movie.objects.all())

            return Response(booked)

        elif not seat_number and movie_title:
            movies = Movie.objects.filter(title=movie_title)

            if not movies.exists():
                return Response({"error": f"Movie '{movie_title}' not found."}, status=status.HTTP_404_NOT_FOUND)

            booked = movie_lists(movies)

            return Response(booked)

        elif not movie_title and seat_number:
            return Response({"error": "You must specify a 'movie' parameter when filtering by seat."}, 
                status=status.HTTP_400_BAD_REQUEST)

        else:
            seat_avail = Booking.objects.filter(seat__seat_number=seat_number,
                movie__title=movie_title).first()

            if seat_avail:
                if seat_avail.seat.booking_status:
                    seat_status = 'booked'
            else:
                seat_status = 'not booked'

            return Response({f"Seat {seat_number} for {movie_title} is {seat_status}."})

    def create(self, request):
        serializer = SeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = serializer.validated_data['movie']
        seat_number = serializer.validated_data['seat_number']
        user = serializer.validated_data['user']

        movie_bookings = Booking.objects.filter(movie=movie)

        seats_taken = movie_bookings.values_list('seat__seat_number', flat=True)
        seat = None

        if seat_number not in [f'{row}{num}' for row in string.ascii_uppercase[:8] for num in range(1, 9)]:
            raise ValidationError({"seat_number": f"Seat {seat_number} Does not exist."})
        # If the seat_number not in list, doesn't exist. We're going to create a new one and add it to the DB
        elif seat_number not in seats_taken:
            seat = Seat.objects.create(seat_number=seat_number, booking_status=True)
        # If the seat is in seats taken, send error.
        else:
            raise ValidationError({"seat_number": f"Seat {seat_number} is already booked for this movie."})

        new_booking = Booking.objects.create(movie=movie, seat=seat, user=user, booking_date=timezone.now())

        return Response({"Seat successfully booked!"}, status=status.HTTP_201_CREATED)

class BookingViewSet(viewsets.ViewSet):
    """Booking Viewset, allows for looking at the history of previous bookings and making new ones"""
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def list(self, request):
        user = request.query_params.get('user')

        if not user:
            return Response({"error": "You must specify a 'user' parameter when looking for history."}, 
                status=status.HTTP_400_BAD_REQUEST)

        else:
            bookings = Booking.objects.filter(user=user)
            serializer = BookingSerializer(bookings, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = serializer.validated_data['movie_title']
        seat_number = serializer.validated_data['seat_number']
        user = serializer.validated_data['user']

        movie_bookings = Booking.objects.filter(movie=movie)

        seats_taken = movie_bookings.values_list('seat__seat_number', flat=True)
        seat = None

        if seat_number not in [f'{row}{num}' for row in string.ascii_uppercase[:8] for num in range(1, 9)]:
            raise ValidationError({"seat_number": f"Seat {seat_number} Does not exist."})
        # If the seat_number not in list, doesn't exist. We're going to create a new one and add it to the DB
        elif seat_number not in seats_taken:
            seat = Seat.objects.create(seat_number=seat_number, booking_status=True)
        # If the seat is in seats taken, send error.
        else:
            raise ValidationError({"seat_number": f"Seat {seat_number} is already booked for this movie."})

        new_booking = Booking.objects.create(movie=movie, seat=seat, user=user, booking_date=timezone.now())

        return Response({"Seat successfully booked!"}, status=status.HTTP_201_CREATED)

# For HTML Rendering
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

    if request.method == 'POST':
        form = HistoryForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            return redirect('booking_history_with_user', user=user)

    else:
        form = HistoryForm()
    
    bookings = None

    if user:
        bookings = Booking.objects.filter(user=user).order_by('booking_date').reverse()

    return render(request, 'bookings/booking_history.html', {'bookings': bookings, 'form': form, 'user': user})

def delete_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    seat = booking.seat
    user = booking.user

    booking.delete()
    seat.delete()

    return redirect('booking_history_with_user', user=user)

