from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api_apps.models import student, Teacher
from api_apps.serializer import StudentSerializer, TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

