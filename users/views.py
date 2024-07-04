import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import User
import json

SOURCE_URL = 'https://reqres.in/api/users'

# class for fetch user based on page
class FetchUsers(APIView):
    def get(self, request):
        page = request.GET.get('page')
        
        # create error response if no query
        if not page:
            return Response({'error': 'Missing query parameter: page'})

        response = requests.get(SOURCE_URL, params={'page': page})
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from source'})

        data = response.json().get('data', [])
        fetched_users = []
        for user_data in data:
            user_id = user_data['id']
            # If user id doesn't exist save data to database
            if not User.objects.filter(id=user_id).exists():
                user = User(
                    id=user_id,
                    email=user_data['email'],
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    avatar=user_data['avatar']
                )
                user.save()
                # Save data for showing in the response
                fetched_users.append({
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'avatar': user.avatar
                })
            else:
                return Response({'error': 'Data id already exists in the database'})
        return Response(fetched_users)

# class for get selected user
class GetUser(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            return Response({
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'avatar': user.avatar,
            })
        except:
            return Response({'error': 'User ID not found'})

class CRUDUsers(APIView):
    # for get all user
    def get(self, request):
        users = User.objects.all()
        users_list = []
        for user in users:
            users_list.append(
                {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'avatar': user.avatar
                }
            )
        return Response(users_list)
    # post one data
    def post(self, request):
        data = json.loads(request.body)
        if User.objects.filter(id=data.get('id')).exists():
            return Response({'error': 'User already exists'})
        user = User(
            id=data['id'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            avatar=data['avatar']
        )
        user.save()
        return Response({
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'avatar': user.avatar
        })
    # update one data
    def put(self, request):
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=data.get('id'))
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.avatar = data['avatar']
            user.updated_at = timezone.now()
            user.save()
            return Response({
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'avatar': user.avatar
            })
        except User.DoesNotExist:
            return Response({'error': 'User not found'})
        
    # Delete one data
    def delete(self, request):
        data = json.loads(request.body)
        auth_header = request.headers.get('Authorization')
        if auth_header != '3cdcnTiBsl':
            return Response({'error': 'Unauthorized'})

        try:
            user = User.objects.get(id=data.get('id'))
            user.deleted_at = timezone.now()
            user.save()
            return Response({'message': f"User ID {data.get('id')} deleted"})
        except User.DoesNotExist:
            return Response({'error': 'User not found'})
