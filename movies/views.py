from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import messages

# Create your views here.
def homepage(request):
	if request.method == "POST":
		movie_form = MovieForm(request.POST, request.FILES)
		if movie_form.is_valid():
			movie_form.save()
			messages.success(request, (f'\"{ movie_form.cleaned_data["movie_title"] }\" was successfully added!'))
			return redirect("homepage")
		else:
			messages.error(request, 'Error saving form')	
	else: 
		movie_form = MovieForm()
	movies = Movie.objects.all()
	return render(request, "movies/home.html", {'movie_form':movie_form, 'movies':movies})