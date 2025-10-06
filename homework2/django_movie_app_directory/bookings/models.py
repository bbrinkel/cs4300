from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    release_date =  models.DateTimeField()
    duration = models.DurationField()

    def __str__(self): 
        return self.title

class Seat(models.Model):
    seat_number = models.CharField(max_length=2)
    booking_status = models.BooleanField(default=False)

    def __str__(self): 
        return self.seat_number

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length = 50)
    booking_date = models.DateTimeField()
