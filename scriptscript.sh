#!/bin/bash

#mkdir logs on logging machine
#mkdir logs on target machine
#in .bashrc on target machine:

test "$(ps -ocommand= -p $PPID | awk '{print $1}')" == 'script' || (script -f $HOME/$(date + "%d-%b-%y_%H-%M-%S")_shell.log) #test whether script is running, if not start script
trap "scp /home/student/*_shell.log kali@$ip:/home/kali/logs; mv /home/student/*_shell.log /home/student/logs" EXIT #when exiting shell, send log to logging machine, move log on target machine to logs dir
