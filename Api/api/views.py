from django.shortcuts import render
from students.models import student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def studentsView(request):
    # students=student.objects.all()  ##query to fetch the data
    # students_list=list(students.values())   #  manual serialization
    

    ##serialization using serializer

    if request.method=='GET':
        #get all data from student table
        students=student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


##fetching the details of the single student using primary key
@api_view(['GET'])   
def studentDetailsView(request,pk):
    try:
        students=student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=StudentSerializer(students)
        return Response(serializer.data,status=status.HTTP_200_OK)