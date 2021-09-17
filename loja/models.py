from django.db import models
# Create your models here.
class Pet(models.Model):
 nome = models.CharField(max_length=100)
 desricao = models.TextField(max_length=100)
 image = models.FileField(upload_to ='static/',blank=True)
