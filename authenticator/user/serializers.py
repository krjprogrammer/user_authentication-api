from rest_framework import serializers
from .models import User_details

class User_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_details
        exclude = ['password']
    