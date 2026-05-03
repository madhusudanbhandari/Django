from django.shortcuts import render
from students.models import student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def studentsView(request):
    # students=student.objects.all()  ##query to fetch the data
    # students_list=list(students.values())   #  manual serialization
    

    ##serialization using serializer

    if request.method=='GET':
        #get all data from student table
        students=student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    

    
