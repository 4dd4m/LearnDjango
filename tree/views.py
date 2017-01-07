from django.shortcuts import render, render_to_response
from . models import Genre
from django.template import RequestContext

def index(request):
    return render(request, 'tree/test.html')

def show_genres(request):
    nodes = Genre.objects.all()
    return render(request, "tree/genres.html",
                          {'nodes': nodes}
                          )


def direction(request):
    return render(request, "tree/compass.html")