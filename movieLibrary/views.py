from django.db import connection
from django.shortcuts import render, redirect  
from movieLibrary.models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.
def main(request):
    return render(request,'main.html')

def add(request):
    return render(request,'add.html')


def home(request):
    movies = Movie.objects.all()  
    return render(request,'home.html',{'movies' :movies})


def movieDetail(request, movieId):
    movieDetails = Movie.objects.get(movieId=movieId)
    return render(request,'movieDetails.html',{'movieDetails' :movieDetails})
