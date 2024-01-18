from .views import user_login,Get_Data,Serialized_data_view,Register,Login,Post_supply_chain_data,Supply_Api_view,Firm_table_data,Firm_data_api_view,Post_product_config_data,Product_config_api_view
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
    path('product_view_api',Product_config_api_view.as_view())
]