from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import time, os, random


def IndexView(request):
    return render(request, 'app/index.html')

def create(request):
    return render(request, 'app/create.html')

def create_active(request):
    name  = random.randint(100,999)
    f = open('/home/minghsuan/Desktop/Job/job.sh','w+')
    f.write("#!/bin/bash\n")
    f.write("#SBATCH --job-name=$jobName\n")
    f.write("#SBATCH --ntasks={}\n".format(8))
    f.write("#SBATCH --cpus-per-task=\n")
    f.write("#SBATCH --mem=1gb\n")
    f.write("#SBATCH --output=/tmp/output.log\n")
    f.write("#SBATCH --partition=COMPUTE1Q\n")
    f.write("#SBATCH --account=root\n" )
    f.write("echo '5'\n")
    f.close()
    time.sleep(3)
    os.system('mv /home/minghsuan/Desktop/Job/job.sh /tmp')
    os.system('sbtach job.sh')
    return HttpResponseRedirect(reverse('app:index')) #The reverse var. is names of path from urls.py