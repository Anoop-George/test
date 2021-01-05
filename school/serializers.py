from rest_framework import serializers
from .models import *


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('name',)


class Officestaffserializer(serializers.ModelSerializer):
    class Meta:
        model = Officestaff
        fields = '__all__'


class Teachersserializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'


class Studentsserializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class Parentsserializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'
