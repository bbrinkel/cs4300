# Needed imports
from django.db import models
import string
from django.core.exceptions import ValidationError

class Movie(models.Model):
    """Movie class model, describes movie, its title, its release date, and duration"""
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    release_date =  models.DateTimeField()
    duration = models.DurationField()

    # Returns movie title
    def __str__(self): 
        return self.title

class Seat(models.Model):
    """Seat Model, describes seat through its number and its booking status"""
    seat_number = models.CharField(max_length=2)
    booking_status = models.BooleanField(default=False)

    def __str__(self): 
        return self.seat_number

    def clean(self):
        """Raises ValidationError if the seat doesn't exist in the range of seats"""
        valid_seats = [f"{row}{num}" for row in string.ascii_uppercase[:8] for num in range(1, 9)]
        if self.seat_number not in valid_seats:
            raise ValidationError({"seat_number": f"Seat {self.seat_number} does not exist."})

class Booking(models.Model):
    """Booking Model, connects a seat to a movie as well as a User and has a date of booking"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length = 50)
    booking_date = models.DateTimeField()
