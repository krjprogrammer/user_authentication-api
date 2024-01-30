from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import User_details,Supply_chain_data,firm_data,Product_config,procurement_decision_api,simulation_demand,supplier_Relationship_table,procurements_fc_table,manufacturing_decision_table
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import User_detail_serializer,Supply_chain_data_serializer,firm_data_serializer,product_config_serializer,procurement_post_serializer,procurement_api_serializer,simulation_demand_serializer,manufacturing_decision_serializer
import hashlib
import requests,random
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
        supplier_dict = {
            'supp_A_gamma': data.get('Supplier_A_Gamma_Quantity', 0),
            'supp_B_gamma': data.get('Supplier_B_Gamma_Quantity', 0),
            'supp_C_gamma': data.get('Supplier_C_Gamma_Quantity', 0),
            'supp_D_gamma': data.get('Supplier_D_Gamma_Quantity', 0),
            'supp_B_delta': data.get('Supplier_B_Delta_Quantity', 0),
            'supp_C_delta': data.get('Supplier_C_Delta_Quantity', 0),
            'supp_D_delta': data.get('Supplier_D_Delta_Quantity', 0),
            'supp_E_delta': data.get('Supplier_E_Delta_Quantity', 0),
            'supp_F_delta': data.get('Supplier_F_Delta_Quantity', 0),
            'supp_D_epsilon': data.get('Supplier_D_Epsilon_Quantity', 0),
            'supp_E_epsilon': data.get('Supplier_E_Epsilon_Quantity', 0),
            'supp_F_epsilon': data.get('Supplier_F_Epsilon_Quantity', 0),
            'supp_G_epsilon': data.get('Supplier_G_Epsilon_Quantity', 0),}
        total_gamma_quantity = sum(filter(None, [supplier_dict['supp_A_gamma'], supplier_dict['supp_B_gamma'], supplier_dict['supp_C_gamma'], supplier_dict['supp_D_gamma']]))
        total_gamma_discount = sum(filter(None, [sub_assembly_discount(supplier_dict['supp_A_gamma'], 12), sub_assembly_discount(supplier_dict['supp_B_gamma'], 14), sub_assembly_discount(supplier_dict['supp_C_gamma'], 13), sub_assembly_discount(supplier_dict['supp_D_gamma'], 22)]))
        total_delta_quantity = sum(filter(None, [supplier_dict['supp_B_delta'], supplier_dict['supp_C_delta'], supplier_dict['supp_D_delta'], supplier_dict['supp_E_delta'], supplier_dict['supp_F_delta']]))
        total_delta_discount = sum(filter(None, [sub_assembly_discount(supplier_dict['supp_B_delta'], 15), sub_assembly_discount(supplier_dict['supp_C_delta'], 16), sub_assembly_discount(supplier_dict['supp_D_delta'], 24), sub_assembly_discount(supplier_dict['supp_E_delta'], 14), sub_assembly_discount(supplier_dict['supp_F_delta'], 13)]))
        total_epsilon_quantity = sum(filter(None, [supplier_dict['supp_D_epsilon'], supplier_dict['supp_E_epsilon'], supplier_dict['supp_F_epsilon'], supplier_dict['supp_G_epsilon']]))
        total_epsilon_discount = sum(filter(None, [sub_assembly_discount(supplier_dict['supp_D_epsilon'], 29), sub_assembly_discount(supplier_dict['supp_E_epsilon'], 20), sub_assembly_discount(supplier_dict['supp_F_epsilon'], 19), sub_assembly_discount(supplier_dict['supp_G_epsilon'], 21)]))

        supp_array = [0, 0, 0, 0, 0, 0, 0]
        for j in supplier_dict:
            letter = j[5]
            index = ord(letter) - 65
            if supplier_dict[j] != 0:
                supp_array[index] = index + 1
            else:
                all_zeros = True
                for k in supplier_dict:
                    if k[5] == letter and supplier_dict[k] != 0:
                        all_zeros = False
                        break
                if all_zeros:
                    supp_array[index] = 0
        admin_id = data['admin_ID']
        simulation_id = data['simulation_id']
        r_obj = {data['firm_id']:supp_array}
        result = supplier_Relationship_table.update_or_insert(admin_id, simulation_id,r_obj)
        start_up_cost = 30000
        ongoing_cost = 5000
        supp_vars = [0,0,0,0,0,0,0]
        if len(result)!=0:
            for l, value in enumerate(result):
                if value == 0:
                    supp_vars[l] = ongoing_cost
                elif value < 0:
                    supp_vars[l] = start_up_cost
                elif value > 0:
                    supp_vars[l] = 0
            fc_table_obj,created_fc = procurements_fc_table.objects.update_or_create(
                admin_ID=data['admin_ID'],
                simulation_id=data['simulation_id'],
                defaults={
                    'supplier_A_FC': supp_vars[0],
                    'supplier_B_FC': supp_vars[1],
                    'supplier_C_FC': supp_vars[2],
                    'supplier_D_FC': supp_vars[3],
                    'supplier_E_FC': supp_vars[4],
                    'supplier_F_FC': supp_vars[5],
                    'supplier_G_FC': supp_vars[6],
                }
            )
            fc_table_obj.save()
        else:
            for l, value in enumerate(supp_array):
                if value == 0:
                    supp_vars[l] = 0
                elif value > 0:
                    supp_vars[l] = start_up_cost
            fc_table_obj,created_fc = procurements_fc_table.objects.update_or_create(
                admin_ID=data['admin_ID'],
                simulation_id=data['simulation_id'],
                defaults={
                    'supplier_A_FC': supp_vars[0],
                    'supplier_B_FC': supp_vars[1],
                    'supplier_C_FC': supp_vars[2],
                    'supplier_D_FC': supp_vars[3],
                    'supplier_E_FC': supp_vars[4],
                    'supplier_F_FC': supp_vars[5],
                    'supplier_G_FC': supp_vars[6],
                }
            )
            fc_table_obj.save()
            
        insert_values = procurement_decision_api(admin_ID = data['admin_ID'],simulation_id = data['simulation_id'],
            firm_id = data['firm_id'],Quarter = data['Quarter'],SAC_Responses = data.get('SAC_responses',{}),
            Alpha = {"units'":data['Alpha_quantity'],"Amount":Alpha_amount},Beta = {"units":data['Beta_quantity'],"Amount":Beta_amount},
            Gamma = {"units":total_gamma_quantity,"Amount":total_gamma_discount},Delta = {"units":total_delta_quantity,"Amount":total_delta_discount},
            Epsilon = {"units":total_epsilon_quantity,"Amount":total_epsilon_discount}
        )
        insert_values.save()
        serialized_decision = serialize('json', [insert_values])[1:-1]
        data['SAC_Responses']['procurement_decision'] = serialized_decision
        updated_value = procurement_decision_api(admin_ID=data['admin_ID'],simulation_id=data['simulation_id'],firm_id=data['firm_id'],
            Quarter=data['Quarter'],SAC_Responses=data['SAC_Responses'],Alpha={"units'": data['Alpha_quantity'], "Amount": Alpha_amount},
            Beta={"units": data['Beta_quantity'], "Amount": Beta_amount},Gamma={"units": total_gamma_quantity, "Amount": total_gamma_discount},Delta={"units": total_delta_quantity, "Amount": total_delta_discount},
            Epsilon={"units": total_epsilon_quantity, "Amount": total_epsilon_discount})
        updated_value.save()
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
    
class post_simulation_demand(APIView):
    def post(self,request):
        data = request.data
        hyperware_amount = data.get('Hyperware',0)
        metaware_amount = data.get('Metaware',0)
        previous_sold_Hyperware_units = 1234532
        previuos_sold_Metaware_units = 1134211
        def growth(previous_sold_units):
            random_value = round(random.uniform(-0.5,0.5),1)
            increment_percent = 2 + (random_value)
            growth_in_units = previous_sold_units + round((previous_sold_units*(increment_percent/100)))
            return growth_in_units
        def emergency_cost(current_units,previous_units):
            growth_units = growth(previous_units)
            variation = abs(current_units-growth_units)
            growth_cost = (growth_units*5)*3 + (growth_units*5)*4 + (growth_units*3) + (growth_units*4)
            Emergency_cost = (variation*5)*4 + (variation*5)*5 + (variation*5)*5 + (variation*5)*12
            return growth_cost + Emergency_cost
    
        if hyperware_amount > growth(previous_sold_Hyperware_units):
            hyperware_emergency_cost = emergency_cost(hyperware_amount,previous_sold_Hyperware_units)
            data['Overall_Hyperware_cost'] = hyperware_emergency_cost
        elif hyperware_amount == None:
            data['Overall_Hyperware_cost'] = None
        else:
            data['Overall_Hyperware_cost'] = (hyperware_amount*5)*3 + (hyperware_amount*5)*4 + (hyperware_amount*3) + (hyperware_amount*4)

        if metaware_amount > growth(previuos_sold_Metaware_units):
            metaware_emergency_cost = emergency_cost(metaware_amount,previuos_sold_Metaware_units)
            data['Overall_Metaware_cost'] = metaware_emergency_cost
        elif metaware_amount == None:
            data['Overall_Metaware_cost'] = None
        else:
            data['Overall_Metaware_cost'] = (metaware_amount*5)*3 + (metaware_amount*5)*4 + (metaware_amount*3) + (metaware_amount*4)
        
        serializer = simulation_demand_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class simulation_demand_api_view(APIView):
    def get(self,request):
        db_data = simulation_demand.objects.all()
        serializer = simulation_demand_serializer(db_data,many=True)
        return Response(serializer.data)

class post_manufacturing_decision_data(APIView):
    def post(self,request):
        data = request.data
        product_0_units = data.get('production_product_0_units',0)
        hyperware_units = data.get('production_hyperware_units',0)
        metaware_units = data.get('production_metaware_units',0)
        if product_0_units!=0:
            data['product_0_info'] = {'Total_units':product_0_units,'alpha_quantity_required':product_0_units*9,'beta_quantity_required':product_0_units*9,'Fixed_cost_per_order':f'${20000}','Labour_cost_per_unit':f'${22}','Labour_cost_according_order':f'${22*product_0_units}','production_cost_per_unit':f'${11}','Production_cost_according_order':f'${11*product_0_units}'}
        else:
            data['product_0_info'] = {}
        if hyperware_units!=0:
            data['product_hyperware_info'] = {'Total_units':hyperware_units,'Manufacturing_Plant':{'Fixed_cost_per_order':f'${22500}','Labour_cost_per_unit':f'${30}','Labour_cost_according_order':f'${hyperware_units*30}','Production_cost_per_unit':f'${20}','Production_cost_acccording_order':f'${20*hyperware_units}'},
                                          'DC1':{'Fixed_cost_per_order':f'${5000}','Labour_cost_per_unit':f'${14}','Labour_cost_according_order':f'${hyperware_units*14}','Production_cost_per_unit':f'${12}','Production_cost_acccording_order':f'${12*hyperware_units}'},
                                          'DC2':{'Fixed_cost_per_order':f'${5000}','Labour_cost_per_unit':f'${15}','Labour_cost_according_order':f'${hyperware_units*15}','Production_cost_per_unit':f'${14}','Production_cost_acccording_order':f'${14*hyperware_units}'},
                                          'DC3':{'Fixed_cost_per_order':f'${4000}','Labour_cost_per_unit':f'${12}','Labour_cost_according_order':f'${hyperware_units*12}','Production_cost_per_unit':f'${11}','Production_cost_acccording_order':f'${11*hyperware_units}'}}
        else:
            data['product_hyperware_info'] = {}
        if metaware_units!=0:
            data['product_metaware_info'] = {'Total_units':metaware_units,'Manufacturing_Plant':{'Fixed_cost_per_order':f'${24500}','Labour_cost_per_unit':f'${36}','Labour_cost_according_order':f'${metaware_units*36}','Production_cost_per_unit':f'${16}','Production_cost_acccording_order':f'${16*metaware_units}'},
                                          'DC1':{'Fixed_cost_per_order':f'${6000}','Labour_cost_per_unit':f'${16}','Labour_cost_according_order':f'${metaware_units*16}','Production_cost_per_unit':f'${10}','Production_cost_acccording_order':f'${10*metaware_units}'},
                                          'DC2':{'Fixed_cost_per_order':f'${8000}','Labour_cost_per_unit':f'${20}','Labour_cost_according_order':f'${metaware_units*20}','Production_cost_per_unit':f'${12}','Production_cost_acccording_order':f'${12*metaware_units}'},
                                          'DC3':{'Fixed_cost_per_order':f'${5000}','Labour_cost_per_unit':f'${15}','Labour_cost_according_order':f'${metaware_units*15}','Production_cost_per_unit':f'${10}','Production_cost_acccording_order':f'${10*metaware_units}'}}
        else:
            data['product_metaware_info'] = {}
        serializer = manufacturing_decision_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class manufacturing_decision_api_view(APIView):
    def get(self,request):
        db_data = manufacturing_decision_table.objects.all()
        serializer = manufacturing_decision_serializer(db_data,many=True)
        return Response(serializer.data)
