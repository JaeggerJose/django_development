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
    
    # Basic infroamtion
    task_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image_type = models.CharField(max_length=50, null=True)
    
    # Task time
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    during_time = models.CharField(max_length=20)
    predict_endtime = models.CharField(max_length=20)
    
    # Conncetion port
    loginport_ftp = models.CharField(max_length=15, null=True)
    loginport_gui_webtop = models.IntegerField(null=True)
    loginport_gui_webide = models.IntegerField(null=True)
    loginport_ssh = models.IntegerField(null=True)
    
    #job details
    jobid = models.CharField(unique=True, null=True, max_length=50)
    mem_num = models.IntegerField(null=True)
    cpu_core = models.IntegerField(null=True)
    gpu_num =  models.IntegerField(null=True)
    
    #status of job
    status_job = models.CharField(max_length=20)
    
    #make the information rendering on the admin website and because jobid is integer we need to change it to string
    def __str__(self):
        return str(self.jobid)

