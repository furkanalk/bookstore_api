from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotAllowed
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
#
from store.serializer import UserSerializer

# Register
@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login
@api_view(['POST'])
def loginUser(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                raise AuthenticationFailed('User NOT found.')

        if not user:
            user = authenticate(username=username, password=password)
            
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Username or password is incorrect.'}, status=status.HTTP_401_UNAUTHORIZED)

# Logout
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logoutUser(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    else:
        return HttpResponseNotAllowed(request.method)
        
