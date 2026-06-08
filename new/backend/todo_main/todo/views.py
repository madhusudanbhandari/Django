from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import RegisterSerializer,TodoSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import todo
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer=RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user=serializer.save()
        return Response({'message':'Registration Successfull',
                         'user':{
                             'username':user.username,
                             'email':user.email,
                             'gender':user.gender,
                             'age':user.age
                         }},status=status.HTTP_201_CREATED)
    print ('Validation Errors',serializer.errors)
    return Response({'message':'Registration Failed'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username=request.data.get('username')
    password=request.data.get('password')

    user=authenticate(username=username,password=password)

    if user is not None:
        refresh=RefreshToken.for_user(user)

        return Response({
            'message':'Login successfull',
            'username':user.username,
            'refresh':str(refresh),
            'access':str(refresh.access_token),
         }, status=status.HTTP_200_OK)
    else:
        
        return Response({
            'message': 'Invalid username or password'
        }, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def todo_register(request):
   

    if request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message':'Todo saved'},
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)    
       

    elif request.method=='GET':
        todos=todo.objects.filter(user=request.user)
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
       

@api_view(['PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def update_todo(request,pk):

    if request.method=='PATCH':
        try:
            todo_item=todo.objects.get(id=pk,user=request.user)
        except todo.DoesNotExist:
            return Response({
                "error":"Todo not found"
            },status=status.HTTP_404_NOT_FOUND)

        serializer=TodoSerializer(
            todo_item,data=request.data,partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif  request.method=='DELETE':
        try:
            todo_item=todo.objects.get(id=pk,user=request.user)
        except todo.DoesNotExist:
            return Response({
                "error":"Todo not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        todo_item.delete()
        return Response({'messsage':'Todo deleted successfully'},status=status.HTTP_404_NOT_FOUND)