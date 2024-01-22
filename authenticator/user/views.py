from django.shortcuts import render
from django.http import HttpResponse
from .models import User_details,Supply_chain_data,firm_data,Product_config,procurement_decision_api
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import User_detail_serializer,Supply_chain_data_serializer,firm_data_serializer,product_config_serializer,procurement_post_serializer,procurement_api_serializer
import hashlib
import requests
def user_login(request):
    return render(request,'index.html')

def Register(request):
    return render(request,'register.html')

def encrypt_pass(password):
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    encoded_password = hash.hexdigest()
    return encoded_password

def Login(request):
    if request.method == 'GET':
        user_name = request.GET.get('username')
        pass_word = request.GET.get('pass')
        encoded_pass = encrypt_pass(pass_word)
        matching_user = User_details.objects.filter(username=user_name, password=encoded_pass)
        if matching_user.exists():
            return HttpResponse('User was Loged in successfully')
        else:
            return HttpResponse('User does not Exists please register')

def Get_Data(request):
    if request.method == 'GET':
        user_name = request.GET.get('username')
        pass_word = request.GET.get('pass')
        e_mail = request.GET.get('email')
        if user_name and pass_word :
            encoded_pass = encrypt_pass(pass_word)
            insert = User_details(username = user_name, password = encoded_pass, email=e_mail)
            insert.save()
            return HttpResponse(f'User with username {user_name} was saved sucessfully')
        else:
            return HttpResponse('Username or Password is missing')

class Serialized_data_view(APIView):
    def get(self,request):
        db_data = User_details.objects.all()
        serializer = User_detail_serializer(db_data,many=True)
        return Response(serializer.data)

class Post_supply_chain_data(APIView):
   def post(self,request):
       data = request.data
       serializer = Supply_chain_data_serializer(data=data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Supply_Api_view(APIView):
    def get(self,request):
        db_data = Supply_chain_data.objects.all()
        serializer = Supply_chain_data_serializer(db_data,many=True)
        return Response(serializer.data)
    
class Firm_table_data(APIView):
    def post(self,request):
        data = request.data
        serializer = firm_data_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Firm_data_api_view(APIView):
    def get(self,request):
        db_data = firm_data.objects.all()
        serializer = firm_data_serializer(db_data,many=True)
        return Response(serializer.data)
    
class Post_product_config_data(APIView):
    def post(self,request):
        data = request.data
        packaging_dict = {
            1:10,2:14,3:28
        }
        hi = 20
        price = (10+0.5*(data['Bandwidth']**3))+(8+3*(data['Warranty']**2))+packaging_dict[data['Packaging']]
        data['Price'] = round(price)
        print(hi,data['Price'])
        serializer = product_config_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Product_config_api_view(APIView):
    def get(self,request):
        db_data = Product_config.objects.all()
        serializer = product_config_serializer(db_data,many=True)
        return Response(serializer.data)

class post_procurement_data(APIView):
    def post(self,request):
        data = request.data
        def raw_material_dicount(quantity,price):
            if 250000 <= quantity <= 500000:
                original_price = quantity*price
                discounted_price = (original_price - original_price*0.076)
                return discounted_price
            elif 500000 < quantity <= 1000000:
                original_price = quantity*price
                discounted_price = (original_price - original_price*0.138)
                return discounted_price
            elif 1000000 < quantity:
                original_price = quantity*price
                discounted_price = (original_price - original_price*0.192)
                return discounted_price
            else:
                return quantity*price
        Alpha_amount = raw_material_dicount(data['Alpha_quantity'],3)
        Beta_amount =  raw_material_dicount(data['Beta_quantity'],4)
        def sub_assembly_discount(quantity,price):
            if 100000 > quantity > 50000:
                original_price = quantity*price
                discounted_price = (original_price - original_price*0.104)
                return discounted_price
            elif quantity > 100000:
                original_price = quantity*price
                discounted_price = (original_price - original_price*0.175)
                return discounted_price
            else:
                return quantity*price
        total_gamma_quantity = sum(filter(None,[data['Supplier_A_Gamma_Quantity'],data['Supplier_B_Gamma_Quantity'],data['Supplier_C_Gamma_Quantity'],data['Supplier_D_Gamma_Quantity']]))
        total_gamma_discount = sum(filter(None,[sub_assembly_discount(data['Supplier_A_Gamma_Quantity'],12),sub_assembly_discount(data['Supplier_B_Gamma_Quantity'],14),sub_assembly_discount(data['Supplier_C_Gamma_Quantity'],13),sub_assembly_discount(data['Supplier_D_Gamma_Quantity'],22)]))
        total_delta_quantity = sum(filter(None,[data['Supplier_B_Delta_Quantity'],data['Supplier_C_Delta_Quantity'],data['Supplier_D_Delta_Quantity'],data['Supplier_E_Delta_Quantity'],data['Supplier_F_Delta_Quantity']]))
        total_delta_discount = sum(filter(None,[sub_assembly_discount(data['Supplier_B_Delta_Quantity'],15),sub_assembly_discount(data['Supplier_C_Delta_Quantity'],16),sub_assembly_discount(data['Supplier_D_Delta_Quantity'],24),sub_assembly_discount(data['Supplier_E_Delta_Quantity'],14),sub_assembly_discount(data['Supplier_F_Delta_Quantity'],13)]))
        total_epsilon_quantity = sum(filter(None,[data['Supplier_D_Epsilon_Quantity'],data['Supplier_E_Epsilon_Quantity'],data['Supplier_F_Epsilon_Quantity'],data['Supplier_G_Epsilon_Quantity']]))
        total_epsilon_discount = sum(filter(None,[sub_assembly_discount(data['Supplier_D_Epsilon_Quantity'],29),sub_assembly_discount(data['Supplier_E_Epsilon_Quantity'],20),sub_assembly_discount(data['Supplier_F_Epsilon_Quantity'],19),sub_assembly_discount(data['Supplier_G_Epsilon_Quantity'],21)]))
        insert_values = procurement_decision_api(
            admin_ID = data['admin_ID'],simulation_id = data['simulation_id'],
            firm_id = data['firm_id'],Quarter = data['Quarter'],SAC_Responses = data.get('SAC_responses',{}),
            Alpha = {"units'":data['Alpha_quantity'],"Amount":Alpha_amount},Beta = {"units":data['Beta_quantity'],"Amount":Beta_amount},
            Gamma = {"units":total_gamma_quantity,"Amount":total_gamma_discount},Delta = {"units":total_delta_quantity,"Amount":total_delta_discount},
            Epsilon = {"units":total_epsilon_quantity,"Amount":total_epsilon_discount}
        )
        insert_values.save()
        serializer = procurement_post_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class procurement_api_view(APIView):
    def get(self,request):
        db_data = procurement_decision_api.objects.all()
        serializer = procurement_api_serializer(db_data,many=True)
        return Response(serializer.data)