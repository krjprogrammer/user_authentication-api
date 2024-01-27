from django.db import models
class User_details(models.Model):
    username = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length = 16)

class Supply_chain_data(models.Model):
    ADMIN_ID = models.IntegerField()
    PRODUCT_DEVELOPMENT = models.BooleanField()
    PROCUREMENT = models.BooleanField()
    MANUFACTURING = models.BooleanField()
    DISTRIBUTION = models.BooleanField()
    TRANSPORTATION = models.BooleanField()
    SERVICE = models.BooleanField()
    DEMAND_GEN = models.BooleanField()
    FORCASTING = models.BooleanField()
    IT = models.BooleanField()
    OTHER = models.BooleanField()
    R_STUDY = models.BooleanField()

class firm_data(models.Model):
    admin_ID = models.IntegerField()
    simulation = models.IntegerField()
    firm1 = models.CharField(max_length=50)
    firm2 = models.CharField(max_length=50)
    firm3 = models.CharField(max_length=50)
    firm4 = models.CharField(max_length=50)
    firm5 = models.CharField(max_length=50)

class Product_config(models.Model):
    admin_ID = models.IntegerField()
    simulation_id = models.IntegerField()
    category = models.CharField(max_length = 1)
    Alpha = models.IntegerField()
    Beta = models.IntegerField()
    Bandwidth = models.IntegerField()
    Warranty = models.IntegerField()
    Packaging = models.IntegerField()
    Price = models.IntegerField()

class procurement_post(models.Model):
    admin_ID = models.IntegerField()
    simulation_id = models.IntegerField()
    firm_id = models.IntegerField()
    Quarter = models.IntegerField()
    SAC_Responses = models.JSONField()
    Alpha_quantity = models.BigIntegerField()
    Beta_quantity = models.BigIntegerField()
    Supplier_A_Gamma_Quantity = models.BigIntegerField(null=True)
    Supplier_B_Gamma_Quantity = models.BigIntegerField(null=True)
    Supplier_C_Gamma_Quantity = models.BigIntegerField(null=True)
    Supplier_D_Gamma_Quantity = models.BigIntegerField(null=True)
    Supplier_B_Delta_Quantity = models.BigIntegerField(null=True)
    Supplier_C_Delta_Quantity = models.BigIntegerField(null=True)
    Supplier_D_Delta_Quantity = models.BigIntegerField(null=True)
    Supplier_E_Delta_Quantity = models.BigIntegerField(null=True)
    Supplier_F_Delta_Quantity = models.BigIntegerField(null=True)
    Supplier_D_Epsilon_Quantity = models.BigIntegerField(null=True)
    Supplier_E_Epsilon_Quantity = models.BigIntegerField(null=True)
    Supplier_F_Epsilon_Quantity = models.BigIntegerField(null=True)
    Supplier_G_Epsilon_Quantity = models.BigIntegerField(null=True)

class procurement_decision_api(models.Model):
    admin_ID = models.IntegerField()
    simulation_id = models.IntegerField()
    firm_id = models.IntegerField()
    Quarter = models.IntegerField()
    SAC_Responses = models.JSONField()
    Alpha = models.JSONField()
    Beta = models.JSONField()
    Gamma = models.JSONField()
    Delta = models.JSONField()
    Epsilon = models.JSONField()

class simulation_demand(models.Model):
    admin_ID = models.IntegerField()
    simulation_id = models.IntegerField()
    firm_id = models.IntegerField()
    Quarter = models.IntegerField()
    Rules = models.JSONField()
    Hyperware = models.BigIntegerField()
    Metaware = models.BigIntegerField()
    Overall_Hyperware_cost = models.BigIntegerField(default=None,null=True)
    Overall_Metaware_cost = models.BigIntegerField(default=None,null=True)

class supplier_Relationship_table(models.Model):
    admin_ID = models.IntegerField()
    simulation_id = models.IntegerField()
    Relation_Object = models.JSONField()
    @classmethod
    def update_or_insert(cls, admin_id, simulation_id, new_relation_object):
        existing_entry = cls.objects.filter(admin_ID=admin_id, simulation_id=simulation_id).first()

        if existing_entry:
            existing_json = existing_entry.Relation_Object
            existing_json.append(new_relation_object)
            existing_entry.Relation_Object = existing_json
            existing_entry.save()
            result = cls.perform_computation(existing_entry,new_relation_object)
            if existing_json:
                existing_json.pop(0)
                existing_entry.save()
            return result

        else:
            new_entry = cls(admin_ID=admin_id, simulation_id=simulation_id, Relation_Object=[new_relation_object])
            new_entry.save()
            return []

    @classmethod
    def perform_computation(cls, existing_entry, new_relation_object):
        existing_array = existing_entry.Relation_Object
        inner_array = [value for inner_dict in existing_array for value in inner_dict.values()][0]
        new_array = list(new_relation_object.values())[0]
        result_array = [int(existing_value) - int(new_value) for existing_value, new_value in zip(inner_array, new_array)]
        return result_array

class procurements_fc_table(models.Model):
    admin_ID = models.IntegerField()
    simulation_id = models.IntegerField()
    supplier_A_FC = models.BigIntegerField()
    supplier_B_FC = models.BigIntegerField()
    supplier_C_FC = models.BigIntegerField()
    supplier_D_FC = models.BigIntegerField()
    supplier_E_FC = models.BigIntegerField()
    supplier_F_FC = models.BigIntegerField()
    supplier_G_FC = models.BigIntegerField()