from django.db import models

# Create your models here.
class Books(models.Model):
    code=models.IntegerField()
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=20)
    category=models.CharField(max_length=200)
    status=models.CharField(max_length=12)
    





