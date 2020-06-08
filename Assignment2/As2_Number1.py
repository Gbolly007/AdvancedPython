# Python version 3.7.6
import os
import time

# Input to receive files from user
command = input('Enter the python scripts seperated by a comma ')
# files are splitted into an array using comma
com = command.split(',')
rank = {}
# for loop to run each file and determine execution time
for c in com:
    # Condition to determine if the particular file
    # in the loop is valid a python file by checking the last 3 characters
    if c[-3:] != '.py':
        print('Not a valid py file')
        exit()
    try:
        f = open(c)
        f.close()
# variable to store start time
        start_time = time.time()
# execution of script
        bf = os.system("python " + c + " 1")
# variable to subtract start time from end time and get execution time
        sec = time.time() - start_time
# each program is stored in a dictionary with its execution time,
# with the program being the key while execution time is the value
        rank[c] = sec
    except IOError:
        print('File not accessible')

# variable to sort dictionary from lowest to highest
rank = {k: v for k, v in sorted(rank.items(), key=lambda item: item[1])}

num = 1
print('PROGRAM | RANK | TIME ELAPSED')
# loop to print items of the dictionary of the program
# and execution time with their respective ranks
for k, v in rank.items():

    print(k+' |' + str(num) + '  |' + str(v) + ' seconds')
    num += 1
