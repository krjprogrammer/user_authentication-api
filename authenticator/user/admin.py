from django.contrib import admin
from .models import User_details
class user_admin(admin.ModelAdmin):
    list_display = ('username','password')
admin.site.register(User_details,user_admin)
# Register your models here.
