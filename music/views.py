from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1>This is music home page</h1>')

# Create your views here.
