from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    release_date =  models.DateTimeField()
    duration = models.DurationField()

class Seat(models.Model):
    seat_number = models.IntegerField(default=0)
    booking_status = models.BooleanField(default=False)

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length = 50)
    booking_date = models.DateTimeField()
