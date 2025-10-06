from django.db import models

class Movie(models.Model):
    """Movie class model, describes movie, its title, its release date, and duration"""
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    release_date =  models.DateTimeField()
    duration = models.DurationField()

    # Raises appropriate errors when Movie model hits edge cases
    def clean(self):
        if self.release_date > timezone.now():
            raise ValidationError("Release date cannot be in the future.")
        
        if self.duration <= timedelta(0):
            raise ValidationError("Duration must be greater than zero.")

        if len(self.title.strip()) < 2:
            raise ValidationError("Movie title must be at least 2 characters long.")

        if len(self.description.strip()) < 2:
            raise ValidationError("Movie description must be at least 2 characters long.")

    # Returns movie title
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
