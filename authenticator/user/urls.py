from .views import user_login,Get_Data,Serialized_data_view,Register,Login,Post_supply_chain_data,Supply_Api_view,Firm_table_data,Firm_data_api_view,Post_product_config_data,Product_config_api_view,post_procurement_data,procurement_api_view,post_simulation_demand,simulation_demand_api_view,post_manufacturing_decision_data,manufacturing_decision_api_view
from django.urls import path
urlpatterns = [
    path('',user_login),
    path('get_data',Get_Data,name='get_data'),
    path('user_data/',Serialized_data_view.as_view()),
    path('register',Register,name='register'),
    path('login',Login,name='login'),
    path('post_supply_data',Post_supply_chain_data.as_view()),
    path('supply_view_api',Supply_Api_view.as_view()),
    path('post_firm_data',Firm_table_data.as_view()),
    path('firm_view_api',Firm_data_api_view.as_view()),
    path('post_product_data',Post_product_config_data.as_view()),
    path('product_view_api',Product_config_api_view.as_view()),
    path('post_procurement',post_procurement_data.as_view()),
    path('procurement_view_api',procurement_api_view.as_view()),
    path('post_simulation_demand',post_simulation_demand.as_view()),
    path('simulation_demand_api',simulation_demand_api_view.as_view()),
    path('post_manufaturing_data',post_manufacturing_decision_data.as_view()),
    path('manufacturing_view_api',manufacturing_decision_api_view.as_view())
]