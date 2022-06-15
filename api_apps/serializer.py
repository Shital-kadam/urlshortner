from rest_framework import serializers

from api_apps.models import student, Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields=('id','f_name','l_name')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields=('id','f_name','l_name','email')