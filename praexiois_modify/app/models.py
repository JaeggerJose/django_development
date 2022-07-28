from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = PhoneNumberField(unique=True, blank=True)
    #make the information rendering on the admin website
    def __str__(self):
        return self.name

class Job(models.Model):
    job = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #reference to the object User and when it was deleted this Job under the User will be deleted too
    jobid = models.IntegerField(unique=True, null=True)
    mem_num = models.IntegerField(null=True),
    cpu_core = models.IntegerField(null=True),
    gpu_num =  models.IntegerField(null=True),
    image_type = models.CharField(max_length=50, null=True),
    #make the information rendering on the admin website and because jobid is integer we need to change it to string
    def __str__(self):
        return str(self.jobid)
