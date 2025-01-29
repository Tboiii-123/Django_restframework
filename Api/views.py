from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
#custom filter file
from .filters import StudentFilter
from django_filters.rest_framework import DjangoFilterBackend

#To use generics
from rest_framework import generics




#Making an update request thats PUT
#http://127.0.0.1:8000/user/<int:id>

#Get all uers
#http://127.0.0.1:8000/


#To filter in the url endpoint
#http://127.0.0.1:8000/user/?age=24



#class TestView(APIView):
    #permission_classes = [IsAuthenticated]  
   
class TestView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
	#The serialser page  
    serializer_class = StudentSerializer
	#For the view of teh filter
    filter_backends = [DjangoFilterBackend]

#The flter custom code
    filterset_class = StudentFilter


   
   
    # serializer_class = StudentSerializer  
   
    # filterset_class = StudentFilter
       
    # def get(self, request, *args, **kwargs):
        
    #    # qs = Student.objects.all()[:5]
    #     qs = Student.objects.all()
        
    #     #We use many is True because we are getting all users in thet database
    #     serializer = StudentSerializer(qs, many=True)
    #     return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestDetailView(APIView):
   # permission_classes = [IsAuthenticated]  # Requires token authentication
    def get(self, request, id, *args, **kwargs):
        student = get_object_or_404(Student, pk=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id, *args, **kwargs):
        student = get_object_or_404(Student, pk=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        student = get_object_or_404(Student, pk=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










'''
lawal
1234
lawalhussein775@gmail.com

'''