from .models import Student
from rest_framework import serializers  
# this is where wwe convert our models to JSON format by serializing it

class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'
        
