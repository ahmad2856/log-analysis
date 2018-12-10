# log-analysis Project

## pre-requirements to run the project
a. Install python in your computer: https://www.python.org/downloads
b. Install git: https://git-scm.com/downloads
c. Vagrant: https://www.vagrantup.com/downloads.html
d. Virtual Machine: https://www.virtualbox.org/wiki/Downloads
e. Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm


###  Create Views in the db

    create view error_logs_view as select date(time),round(100.0*sum(case log.status when '200 OK' 
    then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time) 
    order by "Percent Error" desc;

###  How to run the project?

A.Start up the vagrant (vagrant up).
B.GO to the directory .vagrant by using command (cd .vagrant).
C.Move the project into vagrant machine using command (scp -P 2222 -r ../log-analysis vagrant@127.0.0.1:~/.).
D.After coping the project use the command (vagrant ssh).
E.Go inside project directory using command (cd log-analysis).
F.Enter into log-analysis directory and run log-analysis.py (python3 log-analysis.py).

