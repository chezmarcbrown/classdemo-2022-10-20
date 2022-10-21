from django import forms
from .models import Movie 


# Create your forms here.
class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('movie_title', 'rating', 'release_year', 'director', 'movie_poster', 'movie_plot')
