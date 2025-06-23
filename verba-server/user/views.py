from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import NewUserSerializer,LoginSerializer
from rest_framework.decorators import permission_classes, api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import NewUser
from django.middleware import csrf
from verba import settings
from rest_framework_simplejwt.exceptions import TokenError

# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request,format=None):
    try:
        # user_name = request.data['user_name']
        email = request.data['email']
        # password = request.data['password']
        # password2 = request.data['password2']
        
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"user successfully signed up"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(["POST"])
@permission_classes([AllowAny])
def signin(request,format=None):
    try:
        email= request.data['email']
        password= request.data["password"]
        
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data["email"]
            user = NewUser.objects.get(email=email)
            token = RefreshToken.for_user(user)
            user_data = NewUserSerializer(user)
            data = user_data.data
            # print("user_data = ",user_data.data)
            # print("refresh = ", refresh['refresh'])
            # print("access = ", token)
            data["tokens"] = {"refresh":str(token),"access":str(token.access_token)}
            response = Response()
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value = data['tokens']['refresh'],
                expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            
            response.data ={"message":"logged in user","data":data}
            response.status_code = 200
            
            return response
            # return Response({"message":"logged in user","data":data},status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)    
  
  
  
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request,format=None):
    # refresh_token = request.data.get("refresh",None
    try:
        # if request.data["refresh"]:
        #     refresh_token = request.data["refresh"]
        #     print("refresh from postman = ",refresh_token)
        # else:
        #     refresh_token = request.COOKIES.get("refresh_token")
        #     print("refresh from browser = ",refresh_token)
        refresh_token = request.data.get("refresh") or request.COOKIES.get("refresh_token")

        try:
            token = RefreshToken(refresh_token)
        except:
            raise TokenError("refresh token is invalid, expired, or otherwise not safe to use.")
        token.blacklist()
        return Response({"message":"logged out successfully"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def retrieveUsers(request,format=None):
    try:
        users = NewUser.objects.all()
        serializer = NewUserSerializer(users, many=True)
        return Response({"message":"retrieved users successfully","data":serializer.data},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def retrieveSingleUser(request,pk,format=None):
    try:
        try:
            user = NewUser.objects.get(pk=pk)
            print("user = ",user)
        except NewUser.DoesNotExist: 
            return Response({"message":"user doesn't exist"})
        serializer = NewUserSerializer(instance=user)
        # print("serializer = ",serializer)
        # if serializer.is_valid(raise_exception=True):
        return Response({"message":"retrieved user successfully","data":serializer.data},status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    
        