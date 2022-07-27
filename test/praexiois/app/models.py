from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = PhoneNumberField(blank=True)
    def __str__(self):  #make the information rendering on the admin website
        return self.name
    
class Job(models.Model):
    job = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    #reference to the object User and when it was deleted this Job under the User will be deleted too
    jobid = models.IntegerField(unique=True, null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.jobid #make the information rendering on the admin website
    
class JobDetail(models.Model):
    jobdetail = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    #reference to the object Job and when it was deleted this JobDetail under the Job will be deleted too
    mem_num = models.IntegerField(null=True)
    cpu_core = models.IntegerField(null=True)
    gpu_num =  models.IntegerField(null=True)
    image_type = models.CharField(max_length=50, null=True)