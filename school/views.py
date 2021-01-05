from .models import *
from .serializers import *
from rest_framework import generics


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class LeadDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class OfficestaffListCreate(generics.ListCreateAPIView):
    queryset = Officestaff.objects.all()
    serializer_class = Officestaffserializer


class OfficestaffdDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Officestaff.objects.all()
    serializer_class = Officestaffserializer

class TeachersListCreate(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = Teachersserializer


class TeachersDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = Teachersserializer

class StudentsListCreate(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentsserializer


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentsserializer

class ParentsListCreate(generics.ListCreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = Parentsserializer


class ParentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parents.objects.all()
    serializer_class = Parentsserializer