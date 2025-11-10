from django.forms import ModelForm
from .models import Movies,Users,Reservations
from django import forms

# Create the form class.
class CreateMovieForm(ModelForm):
	class Meta:
		model = Movies
		fields = ['movie_id', 'movie_name', 'movie_location', 'movie_price']
# Create the form class.
class CreateUserForm(ModelForm):
	class Meta:
		model = Users
		fields = ['user_id', 'user_name']

class CreateReservationForm(ModelForm):
	class Meta:
		model = Reservations
		fields = ['reservation_id', 'user_id', 'movie_id', 'reservation_locations', 'number_of_seats']


class DeleteMovieByIDForm(ModelForm):
	class Meta:
		model = Movies
		fields = ['movie_id']

