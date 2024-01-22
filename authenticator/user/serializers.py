from rest_framework import serializers
from .models import User_details,Supply_chain_data,firm_data,Product_config,procurement_post,procurement_decision_api

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

class product_config_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_config
        fields = '__all__'
        extra_kwargs = {
            'Price':{'required':False}
        }

class procurement_post_serializer(serializers.ModelSerializer):
    class Meta:
        model = procurement_post
        fields = '__all__'

class procurement_api_serializer(serializers.ModelSerializer):
    class Meta:
        model = procurement_decision_api
        fields = '__all__'