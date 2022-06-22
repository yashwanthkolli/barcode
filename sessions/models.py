from django.db import models

# Create your models here.
class Sessions(models.Model):
    Issue_No = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='Issue_No')
    Name = models.CharField(max_length=200)
    Job_No = models.CharField(max_length=200)
    Vessel = models.CharField(max_length=20)
    Port_Name = models.CharField(max_length=200)
    Equipment = models.CharField(max_length=200)
    Issue_Date = models.CharField(max_length=10)

class Barcode(models.Model):
    Barcode_No = models.CharField(primary_key=True, max_length=5)
    Name = models.CharField(max_length=200)
    Item_No = models.CharField(max_length=20)