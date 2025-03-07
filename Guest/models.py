from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30)
    user_contact = models.CharField(max_length=30)
    user_address = models.CharField(max_length=50)
    user_password = models.CharField(max_length=30)
    user_photo = models.FileField(upload_to='Assets/User/Photo/')
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_status=models.IntegerField(default=0)


class tbl_designer(models.Model):
    designer_name = models.CharField(max_length=30)
    designer_email = models.CharField(max_length=30)
    designer_contact = models.CharField(max_length=30)
    designer_address = models.CharField(max_length=50)
    designer_photo = models.FileField(upload_to='Assets/User/Photo/')  
    designer_proof = models.FileField(upload_to='Assets/User/Photo/')  
    designer_password = models.CharField(max_length=30)  
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    designer_status=models.IntegerField(default=0)

class tbl_shop(models.Model):
    shop_name = models.CharField(max_length=30)
    shop_email = models.CharField(max_length=30)
    shop_contact = models.CharField(max_length=30)
    shop_address = models.CharField(max_length=30)
    shop_photo = models.FileField(upload_to='Assets/User/Photo/') 
    shop_proof = models.FileField(upload_to='Assets/User/Photo/') 
    shop_password = models.CharField(max_length=30)  
    shop_status=models.IntegerField(default=0)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)



    