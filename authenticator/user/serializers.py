from rest_framework import serializers
from .models import User_details,Supply_chain_data,firm_data

class User_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_details
        exclude = ['password']

class Supply_chain_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = Supply_chain_data
        fields = '__all__'
    
class firm_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = firm_data
        fields = '__all__'