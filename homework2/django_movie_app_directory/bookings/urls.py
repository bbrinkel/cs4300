from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_view, name='movie_list'),
    path('book/<int:movie_id>/', views.book_seat_view, name='book_seat'),
    path('booking-history/<str:user>/', views.booking_history_with_user_view, name='booking_history_with_user'),
    path('booking-history/', views.booking_history_with_user_view, name='booking_history'),
    path('cancel-booking/<int:booking_id>/', views.delete_booking_view, name='cancel_booking'),
]




