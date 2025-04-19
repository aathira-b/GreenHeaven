from django.db import models
from Designer.models import *
from Guest.models import *
from Shop.models import *

# Create your models here.

class tbl_designrequest(models.Model):
   designrequest_date = models.DateField(auto_now_add=True)
   designrequest_todate = models.CharField(max_length=30)
   designrequest_status = models.IntegerField(default=0)
   designrequest_amount = models.CharField(max_length=30)
   user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
   work = models.ForeignKey(tbl_work, on_delete=models.CASCADE)

class tbl_complaint(models.Model):
   complaint_title = models.CharField(max_length=30)
   complaint_description = models.CharField(max_length=30)
   complaint_date = models.DateField(auto_now_add=True)
   complaint_status = models.IntegerField(default=0)
   complaint_replay = models.CharField(max_length=30)
   user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
   shop = models.ForeignKey(tbl_shop, on_delete=models.CASCADE,null=True)
   desginer = models.ForeignKey(tbl_designer, on_delete=models.CASCADE,null=True)

class tbl_feedback(models.Model):
   feedback_content = models.CharField(max_length=30)
   feedback_date = models.DateField(auto_now_add=True) 
   user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)


class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    booking_totalamount = models.CharField(max_length=30)
    booking_adv_amount = models.CharField(max_length=30)
    booking_status = models.IntegerField(default=0)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)

