from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

#system import
import time, os, random, json
from subprocess import getoutput
from datetime import datetime, timedelta


# Darunter ist für Djangorestframework import library
from .serializers import UserSerializer, JobSerializer
from rest_framework.generics import GenericAPIView
from django.db import transaction
from app.models import User, Job

def information_write_database(data, name, user_name, port):
    user_datas = User.objects.get(name = user_name)
    data_job = user_datas.job_set.create(task_name=name, description='matl1ab using Webtop to connect',
                                         image_type=data['imagename'], start_time=datetime.now(), end_time=(datetime.now()+timedelta(days=1)),
                                         during_time='24:00', predict_endtime='now', loginport_gui_webtop=port,
                                         jobid=int(name), mem_num=data['memory'], cpu_core=data['cpu'], gpu_num=data['gpu'],
                                         status_job='shutdown')
    data_job.save()
    return 0

def get_image_type(imagename):
    if imagename == 'webtop_matlab':
        image_types = 'lms025187/webtop_matlab'
    elif imagename == 'webtop_orange3_CLC':
        image_types = 'lms025187/webtop_bio_software'
    elif imagename == 'webtop_itksnap':
        image_types = 'lms025187/webtop_itk'
    elif imagename == 'webtop_itksnap_mitkworkbench_3dslicer':
        image_types = 'lms025187/webtop_image_captioning'
    else:
        image_types = imagename
    return image_types

def file_write_function(data, name, user_group):
    #device Variable
    mem_number = data['memory']
    cpus_per_task = data['cpu']
    ntasks_num = data['gpu']
    image_types = get_image_type(data['imagename'])
    
    #path Variable
    user_name = 'root'
    format_datetime = "%Y%m%d%H%M%S"
    port = getoutput('getAvailablePort')
    fopen_file = '/home/minghsuan/Desktop/Job_queue/job{}.sh'.format(name)
    change_fileowner = 'chown {0} /home/minghsuan/Desktop/Job_queue/job{1}.sh'.format(user_name ,name)
    change_filegroup = 'chown :{0} /home/minghsuan/Desktop/Job_queue/job{1}.sh'.format(user_name ,name)
    change_priority = 'chmod 770 -R /home/minghsuan/Desktop/Job_queue/job{}.sh'.format(name)
    docker_name = '{0}_{1}'.format(user_name, data['imagename'])
    
    #file produce
    f = open(fopen_file,'w+')
    f.write("#!/bin/bash\n")
    f.write("#SBATCH --job-name=job{}\n".format(name))
    f.write("#SBATCH --ntasks={}\n".format(ntasks_num))
    f.write("#SBATCH --cpus-per-task={}\n".format(cpus_per_task))
    f.write("#SBATCH --mem={}gb\n".format(mem_number))
    f.write("#SBATCH --output=/home/minghsuan/Desktop/Job_finished/output{}.log\n".format(name))
    f.write("#SBATCH --partition=COMPUTE1Q\n")
    f.write("#SBATCH --account={}\n".format(user_group))
    f.write('docker run -d --name={0} -e PUID=1000 -e PGID=1000 -e TZ=Asia/Taipei -p {1}:3000 --shm-size="5gb" {2}\n'.format(docker_name, port, image_types))
    f.close()
    
    # change file owner, group and priority
    os.system(change_fileowner)
    os.system(change_filegroup)
    os.system(change_priority)
    
    # Save data into Database.
    information_write_database(data, name, user_group, port)
    return 0

def IndexView(request):
    return render(request, 'build/index.html')

@ensure_csrf_cookie  #make front-end can get csrf token from cookies
def create_active(request):
    data = json.loads(request.body.decode('utf-8')) # get json lib. from frontend post

    #path Variable
    user_group = 'root'
    user_name = 'root'
    format_datetime = "%Y%m%d%H%M%S"
    name  = (datetime.now().strftime(format_datetime)) + str(random.randint(100,999))
    mv_file = 'mv /home/minghsuan/Desktop/Job_queue/job{}.sh /home/minghsuan/Desktop/Job_finished'.format(name)
    sbatch_file = 'su - {0} -c "sbatch /home/minghsuan/Desktop/Job_finished/job{1}.sh"'.format(user_name, name)

    #file produce and execute
    file_write_function(data, name, user_group)

    time.sleep(1)
    os.system(mv_file)
    time.sleep(1) # in order to prevent sending before that sbatch-file produced
    os.system(sbatch_file)

    status_web = {'status' : '200'}
    #return HttpResponseRedirect(reverse('app:index')) #The reverse var. is names of path from urls.py
    return JsonResponse(status_web)


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

#def show_all_job_for_user(request):
    #image_type = data['image_name']
