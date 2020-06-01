# Python version 3.7.6
import os

# Variable to hold command
shlcmd = ""
# Loop condition to check if command is not equals to exit and executes command
while (shlcmd != "exit"):
    # Command from user is stored here
    shlcmd = input('/myshell:')
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
