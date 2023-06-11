from django.db import models

# Create your models here.
class apiModel(models.Model):
    prj_id=models.IntegerField()
    prj_name=models.CharField(max_length=50)
    prj_amt=models.PositiveIntegerField()
    prj_location=models.CharField(max_length=50)

