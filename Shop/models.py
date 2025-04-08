from django.db import models
from Guest.models import *
from Admin.models import *

# Create your models here.
class tbl_product(models.Model):
    product_name=models.CharField(max_length=30)
    product_details=models.CharField(max_length=30)
    product_price=models.CharField(max_length=30)
    product_photo=models.FileField(upload_to='Assets/User/Photo/')
    shop = models.ForeignKey(tbl_shop, on_delete=models.CASCADE,null=True)
    subcategory = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE,null=True)

class tbl_stock(models.Model):
    stock_count=models.CharField(max_length=30)
    stock_date=models.DateField(auto_now_add=True)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE,null=True)    


class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="from_user",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="to_user",null=True)
    shop_from=models.ForeignKey(tbl_shop,on_delete=models.CASCADE,related_name='from_shop',null=True)
    shop_to=models.ForeignKey(tbl_shop,on_delete=models.CASCADE,related_name='to_shop',null=True)
    
    designer_from=models.ForeignKey(tbl_designer,on_delete=models.CASCADE,related_name='from_designer',null=True)
    designer_to=models.ForeignKey(tbl_designer,on_delete=models.CASCADE,related_name='to_designer',null=True)

    shop_from=models.ForeignKey(tbl_shop,on_delete=models.CASCADE,related_name='from_shop',null=True)
    shop_to=models.ForeignKey(tbl_shop,on_delete=models.CASCADE,related_name='to_shop',null=True)
