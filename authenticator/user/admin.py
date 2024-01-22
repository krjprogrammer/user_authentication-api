from django.contrib import admin
from .models import User_details,Supply_chain_data,firm_data,Product_config,procurement_decision_api,procurement_post
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

class procurement_post_admin(admin.ModelAdmin):
    list_display =  ("admin_ID","simulation_id","firm_id","Quarter","SAC_Responses",
        'Alpha_quantity',
        'Beta_quantity',
        'Supplier_A_Gamma_Quantity',
        'Supplier_B_Gamma_Quantity',
        'Supplier_C_Gamma_Quantity',
        'Supplier_D_Gamma_Quantity',
        'Supplier_B_Delta_Quantity',
        'Supplier_C_Delta_Quantity',
        'Supplier_D_Delta_Quantity',
        'Supplier_E_Delta_Quantity',
        'Supplier_F_Delta_Quantity',
        'Supplier_D_Epsilon_Quantity',
        'Supplier_E_Epsilon_Quantity',
        'Supplier_F_Epsilon_Quantity',
        'Supplier_G_Epsilon_Quantity',
    )
admin.site.register(procurement_post,procurement_post_admin)
# Register your models here.
