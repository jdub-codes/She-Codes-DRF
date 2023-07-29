from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:        
        model = apps.get_model('projects.Project')
        fields ='__all__'