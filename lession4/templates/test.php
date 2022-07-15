<?php
    //use empty to check is the form empty or not
    if (empty($_GET['memvalue']) || empty($_GET['cputhread'])) {
        echo "failed informantion sending!";
        exit();
    };
    //get info from the method of GET of form latest form input
    echo "Bueno! You need so much memory(ies)".$_GET['memvalue']." and so much cpu thread(s)".$_GET['cputhread']."<br>";
    echo "And you need ".$_GET['cpucore']." cpu core(s).";
    print_r($_GET);
?>