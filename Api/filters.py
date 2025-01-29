from django_filters import rest_framework as filters
from .models import Student


#The class name should inherit from the filters
class StudentFilter(filters.FilterSet):
    #Charfield os for accepting string value
    #lookup_expr = 'icontains' is like caseinsensitive
    #field_name is the name of the key u wanna search for
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    age = filters.NumberFilter(field_name='age')

    class Meta:
        model = Student
        fields = ['name','age']


#It should be accesed in the api with
#?name_of_field =value
#http://127.0.0.1:8000/api/students/?age=25

