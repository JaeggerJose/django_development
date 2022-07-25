from time import sleep
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import time, os


def IndexView(request):
    return render(request, 'app/index.html')

def create(request):
    return render(request, 'app/create.html')

def create_active(request):
    f = open('/home/minghsuan/Desktop/Job/job.sh','w+')
    f.write("#!/bin/bash\n")
    f.write("#SBATCH --job-name=$jobName\n")
    f.write("#SBATCH --ntasks=1\n")
    f.write("#SBATCH --cpus-per-task=1\n")
    f.write("#SBATCH --mem=1gb\n")
    f.write("#SBATCH --output=/home/minghsuan/Desktop/Job/output.log\n")
    f.write("#SBATCH --partition=COMPUTE1Q\n")
    f.write("#SBATCH --account=root\n" )
    f.write("echo '5'\n")
    f.close()
    time.sleep(2) 
    os.system('sbatch /home/minghsuan/Desktop/Job/job.sh')
    return render(request, 'app/index.html')
