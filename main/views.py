from django.http import JsonResponse
from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

def home(request):
    return JsonResponse({'message': 'Welcome to the Trip API'})

class MeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            access_token = AccessToken(request.META.get('HTTP_AUTHORIZATION').split(' ')[1])        
            user_id = access_token['user_id']
            User = get_user_model()
            user = User.objects.get(id=user_id) 

            return JsonResponse({'user_id': user_id , 'username': user.username, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})
        except Exception as e:
            return JsonResponse({'error': 'Invalid token'}, status=401)
