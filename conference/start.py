#!/usr/bin/python
import os
class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

print bcolors.HEADER + "\nStarting all services...\n" + bcolors.ENDC     

print bcolors.OKBLUE + "\nWaking up MySQL database...\n" + bcolors.ENDC
is_started = os.system("systemctl is-active mysql")
if is_started == 0:
    print bcolors.WARNING + "\nMySQL database is already started, nothing to do here...\n" + bcolors.ENDC
else:
    print bcolors.WARNING + "\nMySQL database is inactive, activating...\n" + bcolors.ENDC
    db = os.system("sudo systemctl start mysql")
    if db == 0:
        print bcolors.OKGREEN + "\nOK.\n" + bcolors.ENDC
    else:
        print bcolors.FAIL + "\nFail.\n" + bcolors.ENDC

print bcolors.OKBLUE + "\nSynchronizing Django with database...\n" + bcolors.ENDC
syn = os.system("python2 manage.py syncdb")
if syn == 0:
    print bcolors.OKGREEN + "\nOK.\n" + bcolors.ENDC
else:
    print bcolors.FAIL + "\nFail.\n" + bcolors.ENDC

f = raw_input(bcolors.WARNING + "\nShould I start Django server now (yes|no)? " + bcolors.ENDC)
if f == 'yes' or f == 'y':
    print bcolors.OKBLUE + "\nStarting Django server...\n" + bcolors.ENDC
    ser = os.system("python2 manage.py runserver")
    if ser == 0:
        print bcolors.OKGREEN + "\nOK.\n" + bcolors.ENDC
    else:
        print bcolors.FAIL + "\nFail.\n" + bcolors.ENDC
else:
    print bcolors.FAIL + "\nNOT Starting Django server\n" + bcolors.ENDC

k = raw_input(bcolors.WARNING + "\nShould I close MySQL after you (yes|no)? " + bcolors.ENDC)
if k == 'yes' or k == 'y':
    print bcolors.OKBLUE + "\nClosing MySQL...\n" + bcolors.ENDC
    db = os.system("sudo systemctl stop mysql")
    if db == 0:
        print bcolors.OKGREEN + "\nOK.\n" + bcolors.ENDC
    else:
        print bcolors.FAIL + "\nFail.\n" + bcolors.ENDC
else:
    print bcolors.FAIL + "\nNOT Closing MySQL\n"

print bcolors.HEADER + "\nOK. I finished my job.\n" + bcolors.ENDC    

