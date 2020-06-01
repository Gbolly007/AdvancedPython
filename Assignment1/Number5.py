# Python version 3.7.6
import sys
import datetime
import os
import psutil
import subprocess

cmd = ''

# Method to get current working directory and format it


def getcwd():
    cwd = subprocess.os.getcwd()
    cwd_arr = cwd.split('/')
    i = 0
    for c in cwd_arr:
        if len(c) == 0:
            cwd_arr.pop(i)
        i += 1

    fwd_slash = '/'

    for cw in cwd_arr:
        fwd_slash = fwd_slash + cw[:1] + '/'

    cmd = "[" + fwd_slash[:-1] + "]:"
    print(cmd)
    return cmd


def logger(frm):
    # Method to create file if it does not exist in the current working directory and append to it
    f = open("myshell.log", "a+")
    # Variable that holds the current pid
    pid = subprocess.os.getpid()
    p = psutil.Process(pid)
    # Variable that holds the current date and time of execution of pid
    dt = datetime.datetime.fromtimestamp(
        p.create_time()).strftime("%Y-%m-%d %H:%M")
    fr_cmd = frm.split(" ")
    if len(fr_cmd) == 1:
        tob = dt + " " + " cmd: " + \
            fr_cmd[0] + " arg: " + " pid: " + str(pid) + "\n"
    elif len(fr_cmd) > 1:
        tob = dt + " " + "cmd: " + fr_cmd[0] + " arg: " + \
            fr_cmd[1] + " pid: " + str(pid) + "\n"
    f.write(tob)
    f.close()


# Variable to hold command
shlcmd = ""
# Variable that holds the current working directory
curwordir = getcwd()
# Loop condition to check if command is not equals to exit and executes command
while (shlcmd != "exit"):
    # Command from user is stored here

    shlcmd = input(curwordir)
    shlcmd = shlcmd.lstrip().rstrip()
    # This block of if condition checks to see if the user wants to change directory with the cd command
    if shlcmd[0:3] == "cd ":
        formated = shlcmd[3:]
    # Check to see if the directory to be changed to exist
        if subprocess.os.path.exists(formated):
            subprocess.os.chdir(formated)
            formatted_loc = formated.split('/')
            chr = '/'
            j = 0
            for a in formatted_loc:
                if len(a) == 0:
                    formatted_loc.pop(j)
                j += 1

            for a in formatted_loc:
                if '.' in a:
                    chr = chr + a[:2] + '/'
                else:
                    chr = chr + a[:1] + '/'
            logger(shlcmd)
            curwordir = "[" + chr[:-1] + "]:"

        else:
            # logging error info into stderr file
            f = open("myshell.stderr", "a+")
            f.write("Directory does not exist \n")
            f.close()
    # Else condition that executes other shell commands apart from cd
    else:
        # Result of execution of command is stored here
        stdout = subprocess.os.popen(shlcmd.strip())
    # Variable to reads each result line from variable stdout
        txt = " "

    # Loop to print line by line
        while txt:
            txt = stdout.read()
            print(txt)
        logger(shlcmd)
        stdout.close()


print("Goodbye")

# Method that logs into myshell.log
