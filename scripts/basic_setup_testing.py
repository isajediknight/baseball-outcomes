
import datetime,time,os,sys,unittest

if(sys.platform.lower().startswith('linux')):
    OS_TYPE = 'linux'
elif(sys.platform.lower().startswith('mac')):
    OS_TYPE = 'macintosh'
elif(sys.platform.lower().startswith('win')):
    OS_TYPE = 'windows'
else:
    OS_TYPE = 'invalid'

# Get our current directory
OUTPUT_FILE_DIRECTORY = os.getcwd()

def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    Last Update: 03/01/2017
    By: LB023593
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

# Create variables for all the paths
if((OS_TYPE == 'windows')):
    # Clear Screen Windows
    os.system('cls')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'\\'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\outputs\\'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\scripts\\'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\classes\\'
    TESTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\tests\\'
    STATIC_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\static\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
    os.system('clear')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'/'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/outputs/'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/inputs/'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/scripts/'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/classes/'
    TESTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/tests/'
    STATIC_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/inputs/static/'

# OS Compatibility for importing Class Files
if((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    sys.path.insert(0,'../classes/')
    sys.path.insert(0, '../modules/')
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')
    sys.path.insert(0, '..\\modules\\')

# < --- Begin Built In Classes Import --- >
import random
# < ---  End  Built In Classes Import --- >

# < --- Begin Custom Classes Import --- >
# Benchmark for tracking the time it takes for the programs tasks
from benchmark import *
# Stadium Class
from stadium import *
# < ---  End  Custom Classes Import --- >

# Record Total Runtime of the program
total_runtime = Benchmark()

# Read in all 30 MLB Stadiums
stadium_input_runtime = Benchmark()
readfile = open(STATIC_DIR+'stadiums.tab','r')
stadiums = []
counter = 0
for line in readfile:
    if(counter != 0):
        my_line = line.split('\t')
        my_line[-1] = my_line[-1].strip()
        stadiums.append(Stadium(*my_line))
    counter += 1
readfile.close()
stadium_input_runtime.stop()
print(str(len(stadiums))+" Stadiums Read In: " + stadium_input_runtime.human_readable_string())

total_runtime.stop()
print("Total Runtime: " + total_runtime.human_readable_string())
