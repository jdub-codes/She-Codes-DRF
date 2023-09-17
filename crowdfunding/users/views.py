from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAdminUser

from .models import CustomUser
from .serializers import CustomUserSerializer

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CustomUserList(APIView):
    permission_classes = [IsAdminUser | AllowAny]

    def get(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            users = CustomUser.objects.all()
        else:
            users = CustomUser.objects.none()

        serializer = CustomUserSerializer(users, many=True)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        # Allow anyone to create a new user
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )


class CustomUserDetail(APIView):
    permission_classes = [IsOwnerOrAdmin]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            if not request.user.is_superuser and request.user != user:
                return Response({"error": "You don't have permission to update this profile."},
                                status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        user_id = user.id
        is_login = user.is_authenticated
        
        return Response({
            'token': token.key,
            'user_id': user_id,
            'is_login': is_login,
        })