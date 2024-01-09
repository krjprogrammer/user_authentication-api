from .views import user_login,Get_Data,Serialized_data_view,Register,Login
from django.urls import path
urlpatterns = [
    path('',user_login),
    path('get_data',Get_Data,name='get_data'),
    path('user_data/',Serialized_data_view.as_view()),
    path('register',Register,name='register'),
    path('login',Login,name='login')
]