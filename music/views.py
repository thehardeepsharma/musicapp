from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Album, Song

class IndexView(ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'
	def get_queryset(self):
		return Album.objects.all()


class DetailView(DetailView):
	model = Album
	template_name = 'music/detail.html'


class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_title', 'genre','album_logo']