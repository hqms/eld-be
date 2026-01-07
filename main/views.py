from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return JsonResponse({'message': 'Welcome to the Trip API'})