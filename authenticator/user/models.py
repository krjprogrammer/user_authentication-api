from django.db import models
class User_details(models.Model):
    username = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length = 16)

