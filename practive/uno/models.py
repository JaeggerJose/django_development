from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    id = models.AutoField(auto_created=True, primary_key=True)
    email = models.EmailField(unique=True)