from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    #To make a field name optional we do this
    #name =serializers.CharField(required=False)

    class Meta:
        model =Student
        fields =('name','age')






