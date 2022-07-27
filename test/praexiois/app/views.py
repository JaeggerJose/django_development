from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import time, os, random

# Darunter ist für Djangorestframework import library
from .serializers import UserSerializer, JobSerializer
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from django.db import transaction
from .models import User, Job, JobDetail


def IndexView(request):
    return render(request, 'app/index.html')

def create(request):
    return render(request, 'app/create.html')

def create_active(request):
    name  = random.randint(100,999)
    f = open('/home/minghsuan/Desktop/Job_queue/job.sh','w+')
    f.write("#!/bin/bash\n")
    f.write("#SBATCH --job-name=$jobName\n")
    f.write("#SBATCH --ntasks={}\n".format(8))
    f.write("#SBATCH --cpus-per-task=\n")
    f.write("#SBATCH --mem=1gb\n")
    f.write("#SBATCH --output=/tmp/output.log\n")
    f.write("#SBATCH --partition=COMPUTE1Q\n")
    f.write("#SBATCH --account=root\n" )
    f.write("echo '1'\n")
    f.close()
    time.sleep(3)
    os.system('mv /home/minghsuan/Desktop/Job_queue/job.sh /home/minghsuan/Desktop/Job_finished')
    os.system('sbtach /home/minghsuan/Desktop/Job_finished/job.sh')
    return HttpResponseRedirect(reverse('app:index')) #The reverse var. is names of path from urls.py


# Darunter ist für Djangorestframework Viewsclass
class UsersView(GenericAPIView):    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **krgs):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)    
    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data)
    
class JobsView(GenericAPIView):    
    queryset = Job.objects.all()
    serializer_class = JobSerializer
      
    def get(self, request, *args, **krgs):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)    
    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data)