from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CreateMovieForm,CreateUserForm,CreateReservationForm
from .models import Movies,Users,Reservations


def index(request):
	return render(request,'index.html')

def list_movies(request):
	movies = Movies.objects.all()
	return render(request, 'list_movies.html', {'movies': movies})

def list_users(request):
	users = Users.objects.all()
	return render(request, 'list_users.html', {'users': users})

def list_reservations(request):
	reservations = Reservations.objects.all()
	return render(request, 'list_reservations.html', {'reservations': reservations})


def reservation(request):
	if request.method == 'POST':
		form = CreateReservationForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'index.html')
	else:
		form = CreateReservationForm()
	return render(request, 'reservation.html', {'form': form})

def add_movie(request):
	if request.method == 'POST':
		form = CreateMovieForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'index.html')
	else:
		form = CreateMovieForm()
	return render(request, 'add_movie.html', {'form': form})

def add_user(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'index.html')
	else:
		form = CreateUserForm()
	return render(request, 'add_user.html', {'form': form})

def delete_movie_by_id(request):
	if request.method == 'POST':
		movie_id = request.POST.get('movie_id')
		movie = Movies.objects.get(movie_id=movie_id)
		movie.delete()
		return render(request, 'index.html')
	else:
		return render(request, 'index.html')