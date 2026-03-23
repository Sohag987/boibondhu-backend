from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def home(request):
    return HttpResponse("Welcome to Boibondhu API!")