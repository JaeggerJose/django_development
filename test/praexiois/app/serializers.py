from .models import User, Job, JobDetail
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'
         
class JobSerializer(serializers.ModelSerializer):
     class Meta:
         model = Job
         fields = '__all__'

class JobDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model = JobDetail
         fields = '__all__'