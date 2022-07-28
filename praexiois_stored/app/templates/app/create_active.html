<?php

    $cpucore = $_POST['cpucore'];
    $cpucore = 1;
    echo $cpucore."<br>";
    $gpu = $_POST['gpu'] = 1;
    echo "$gpu<br>";
    $mem = $_POST['mem'] = 1;
    echo "$mem<br>";
    $nowtime = time();
    $containerName = date("dmYHis", $nowtime).random_int(100,999);
    echo $containerName;
    $port = 3000;
    $jobName = "job".$containerName;

    $cmd = "docker run -p $port:3000 --name=docker$containerName ghcr.io/linuxserver/webtop:ubuntu-xfce";
    echo '<br>'.$cmd;

    $file = fopen("/home/minghsuan/praexisio-web/job_queue/$jobName.sh","w+");
    echo fwrite($file,"#!/bin/bash
#SBATCH --job-name=$jobName
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1gb
#SBATCH --output=output.log
#SBATCH --partition=COMPUTE1Q
#SBATCH --account=root
echo '5' ");
     fclose($file);

?>

