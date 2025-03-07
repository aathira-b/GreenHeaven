from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_adminregister(models.Model):
    adminregister_name=models.CharField(max_length=50)
    adminregister_email=models.CharField(max_length=50)
    adminregister_password=models.CharField(max_length=50)
class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name =models.CharField(max_length=50)
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)

# class tbl_product(models.Model):
#     product_name=models.CharField(max_length=50)
#     product_price=models.CharField(max_length=50)
#     product_details=models.CharField(max_length=50)
#     subcategory = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
#     product_photo = models.FileField(upload_to='Assets/User/Photo/')

