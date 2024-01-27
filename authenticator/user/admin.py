from django.contrib import admin
from .models import User_details,Supply_chain_data,firm_data,Product_config,procurement_decision_api,simulation_demand,supplier_Relationship_table,procurements_fc_table
class user_admin(admin.ModelAdmin):
    list_display = ('username','password')
admin.site.register(User_details,user_admin)

class supply_admin(admin.ModelAdmin):
    list_display = ('ADMIN_ID','PRODUCT_DEVELOPMENT','PROCUREMENT','MANUFACTURING','DISTRIBUTION','TRANSPORTATION','SERVICE','DEMAND_GEN','FORCASTING','IT','OTHER','R_STUDY')
admin.site.register(Supply_chain_data,supply_admin)

class firm_admin(admin.ModelAdmin):
    list_display = ('admin_ID','simulation','firm1','firm2','firm3','firm4','firm5')
admin.site.register(firm_data,firm_admin)

class product_admin(admin.ModelAdmin):
    list_display = ( "admin_ID","simulation_id","category","Alpha","Beta","Bandwidth","Warranty","Packaging","Price")
admin.site.register(Product_config,product_admin)

class procurement_admin(admin.ModelAdmin):
    list_display = ("admin_ID","simulation_id","firm_id","Quarter","SAC_Responses","Alpha","Beta","Gamma","Delta","Epsilon")
admin.site.register(procurement_decision_api,procurement_admin)

class simulation_demand_admin(admin.ModelAdmin):
    list_display = ('admin_ID', 'simulation_id', 'firm_id', 'Quarter', 'Rules', 'Hyperware', 'Metaware')
admin.site.register(simulation_demand,simulation_demand_admin)

class relation_admin(admin.ModelAdmin):
    list_display = ('admin_ID', 'simulation_id','Relation_Object')
admin.site.register(supplier_Relationship_table,relation_admin)

class procurement_fc_admin(admin.ModelAdmin):
    list_display = ("admin_ID",'simulation_id','supplier_A_FC','supplier_B_FC','supplier_C_FC','supplier_D_FC','supplier_E_FC','supplier_F_FC','supplier_G_FC')
admin.site.register(procurements_fc_table,procurement_fc_admin)
# Register your models here.
