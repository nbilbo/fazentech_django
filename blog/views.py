from django.shortcuts import render
from django.views.generic import DetailView, ListView


def index(request):
	return render(request, 'blog/index.html')
