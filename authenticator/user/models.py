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