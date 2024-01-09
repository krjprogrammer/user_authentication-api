from django.shortcuts import render
from django.http import HttpResponse
from .models import User_details
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import User_detail_serializer
def user_login(request):
    return render(request,'index.html')

def Register(request):
    return render(request,'register.html')

def Login(request):
    if request.method == 'GET':
        user_name = request.GET.get('username')
        pass_word = request.GET.get('pass')
        matching_user = User_details.objects.filter(username=user_name, password=pass_word)
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
            insert = User_details(username = user_name, password = pass_word, email=e_mail)
            insert.save()
            return HttpResponse(f'User with username {user_name} was saved sucessfully')
        else:
            return HttpResponse('Username or Password is missing')

class Serialized_data_view(APIView):
    def get(self,request):
        db_data = User_details.objects.all()
        serializer = User_detail_serializer(db_data,many=True)
        return Response(serializer.data)

