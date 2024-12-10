from django.shortcuts import render
from .models import Student
from .converter import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# Get request for all students
@api_view(['GET'])
def getstudents(request):
    students = Student.objects.all()
    serial = StudentSerializer(students, many=True)
    return Response(serial.data)

# Post request for a student
# allows api to create record
@api_view(['POST'])
def createstudent(request):
    serial = StudentSerializer(data = request.data)
    if serial.is_valid():
        serial.save()
        return Response(serial.data, status=status.HTTP_201_CREATED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

