from django.contrib import admin
from app.models import User, Job, JobDetail
# Register your models here.

admin.site.register(User)
admin.site.register(Job)
admin.site.register(JobDetail)

