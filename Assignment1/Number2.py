# Python version 3.7.6
import os


cmd = ''

# Method to get current working directory and format it


def getcwd():
    cwd = os.getcwd()
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


# Variable to hold command
shlcmd = ""
curwordir = getcwd()
# Loop condition to check if command is not equals to exit and executes command
while (shlcmd != "exit"):
    # Command from user is stored here

    shlcmd = input(curwordir)
    # This block of if condition checks to see if the user wants to change directory with the cd command
    if shlcmd[0:3] == "cd ":
        formated = shlcmd[3:]
    # Check to see if the directory to be changed to exist
        if os.path.exists(formated):
            os.chdir(formated)
            formatted_loc = formated.split('/')
            chr = '/'
            j = 0
            for a in formatted_loc:
                if len(a) == 0:
                    formatted_loc.pop(j)
                j += 1

            for a in formatted_loc:
                if '.' in a:
                    print(a)
                    chr = chr + a[:2] + '/'
                else:
                    chr = chr + a[:1] + '/'

            curwordir = "[" + chr[:-1] + "]:"
        else:
            print('Directory does not')
    else:
        # Result of execution of command is stored here
        stdout = os.popen(shlcmd.strip())
    # Variable to reads each result line from variable stdout
        txt = " "
    # Loop to print line by line
        while txt:
            txt = stdout.read()
            print(txt)
        stdout.close()

print("Goodbye")
