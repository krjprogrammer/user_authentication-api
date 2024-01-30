from rest_framework import serializers
from .models import User_details,Supply_chain_data,firm_data,Product_config,procurement_post,procurement_decision_api,simulation_demand,manufacturing_decision_table

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
        extra_kwargs = {
            "Supplier_A_Gamma_Quantity":{'required':False,'default':None},
            "Supplier_B_Gamma_Quantity":{'required':False,'default':None},
            "Supplier_C_Gamma_Quantity":{'required':False,'default':None},
            "Supplier_D_Gamma_Quantity":{'required':False,'default':None},
            "Supplier_B_Delta_Quantity":{'required':False,'default':None},
            "Supplier_C_Delta_Quantity":{'required':False,'default':None},
            "Supplier_D_Delta_Quantity":{'required':False,'default':None},
            "Supplier_E_Delta_Quantity":{'required':False,'default':None},
            "Supplier_F_Delta_Quantity":{'required':False,'default':None},
            "Supplier_D_Epsilon_Quantity":{'required':False,'default':None},
            "Supplier_E_Epsilon_Quantity":{'required':False,'default':None},
            "Supplier_F_Epsilon_Quantity":{'required':False,'default':None},
            "Supplier_G_Epsilon_Quantity":{'required':False,'default':None}
        }

class procurement_api_serializer(serializers.ModelSerializer):
    class Meta:
        model = procurement_decision_api
        fields = '__all__'

class simulation_demand_serializer(serializers.ModelSerializer):
    class Meta:
        model = simulation_demand
        fields = '__all__'
        extra_kwargs = {
            'Overall_Hyperware_cost':{'required':False,'default':None},
            'Overall_Metaware_cost':{'required':False,'default':None}
        }

class manufacturing_decision_serializer(serializers.ModelSerializer):
    class Meta:
        model = manufacturing_decision_table
        fields = '__all__'
        extra_kwargs = {
            'production_product_0_units':{'required':False,'default':None},
            'production_hyperware_units':{'required':False,'default':None},
            'produntion_metaware_units':{'required':False,'default':None},
            'product_0_info':{'required':False,'default':None},
            'product_hyperware_info' : {'required':False,'default':None},
            'product_metaware_info' : {'required':False,'default':None}
        } 