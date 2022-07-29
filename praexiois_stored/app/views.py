from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import time, os, random
from datetime import datetime

# Darunter ist für Djangorestframework import library
from .serializers import UserSerializer, JobSerializer
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from django.db import transaction
from app.models import User, Job


def IndexView(request):
    return render(request, 'app/index.html')

def create(request):
    return render(request, 'app/create.html')

def create_active(request):
    #device Variable
    mem_number =1
    cpus_per_task =1
    ntasks_num =8
    #path Variable
    user_name = 'root'
    format_datetime = "%Y%m%d%H%M%S"
    name  = (datetime.now().strftime(format_datetime)) + str(random.randint(100,999))
    fopen_file = '/home/minghsuan/Desktop/Job_queue/job{}.sh'.format(name)
    mv_file = 'mv /home/minghsuan/Desktop/Job_queue/job{}.sh /home/minghsuan/Desktop/Job_finished'.format(name)
    sbatch_file = 'sbatch /home/minghsuan/Desktop/Job_finished/job{}.sh'.format(name)

    #file produce and execute
    f = open(fopen_file,'w+')
    f.write("#!/bin/bash\n")
    f.write("#SBATCH --job-name=job{}\n".format(name))
    f.write("#SBATCH --ntasks={}\n".format(ntasks_num))
    f.write("#SBATCH --cpus-per-task={}\n".format(cpus_per_task))
    f.write("#SBATCH --mem={}gb\n".format(mem_number))
    f.write("#SBATCH --output=/home/minghsuan/Desktop/Job_finished/output{}.log\n".format(name))
    f.write("#SBATCH --partition=COMPUTE1Q\n")
    f.write("#SBATCH --account={}\n".format(user_name))
    f.write("echo '1'\n")
    f.close()
    # Save data in d.b.
    user_datas = User.objects.get(name = user_name)
    data_job = user_datas.job_set.create(jobid = int(name), mem_num = mem_number, cpu_core=cpus_per_task,)
    data_job.save()
    time.sleep(3) ## in order to prevent sending before that sbatch-file produced
    os.system(mv_file)
    time.sleep(1)
    os.system(sbatch_file)

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
