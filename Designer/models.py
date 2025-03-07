from django.db import models
from Guest.models import *

# Create your models here.
class tbl_work(models.Model):
    work_name = models.CharField(max_length=30)
    work_details = models.CharField(max_length=30)
    work_photo = models.FileField(max_length=30)
    designer = models.ForeignKey(tbl_designer, on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    gallery_photo = models.FileField(max_length=30)  
    work = models.ForeignKey(tbl_work, on_delete=models.CASCADE) 



 
  
