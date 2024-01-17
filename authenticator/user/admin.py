from django.contrib import admin
from .models import User_details,Supply_chain_data,firm_data
class user_admin(admin.ModelAdmin):
    list_display = ('username','password')
admin.site.register(User_details,user_admin)

class supply_admin(admin.ModelAdmin):
    list_display = ('ADMIN_ID','PRODUCT_DEVELOPMENT','PROCUREMENT','MANUFACTURING','DISTRIBUTION','TRANSPORTATION','SERVICE','DEMAND_GEN','FORCASTING','IT','OTHER','R_STUDY')
admin.site.register(Supply_chain_data,supply_admin)

class firm_admin(admin.ModelAdmin):
    list_display = ('admin_ID','simulation','firm1','firm2','firm3','firm4','firm5')
admin.site.register(firm_data,firm_admin)
# Register your models here.
