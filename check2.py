"""
Tests BAIS:6060 Homework 1 lasers_small.csv
"""

import sys
import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
FILE_STUD_PATH = os.path.join(BASE_PATH, 'lasers_small.csv')
FILE_ANS_PATH = os.path.join(BASE_PATH, 'a.csv')

        
def fcmp(f1,f2):
    
    # Open File in Read Mode
    file_1 = open(f1, 'r')
    file_2 = open(f2, 'r')

    file_1_line = file_1.readline()
    file_2_line = file_2.readline()
    
    while file_1_line != '' or file_2_line != '':
    
    	# Removing whitespaces
    	file_1_line = file_1_line.rstrip()
    	file_2_line = file_2_line.rstrip()
    
    	# Compare the lines from both file
    	if file_1_line != file_2_line:
            file_1.close()
            file_2.close()
            return(False)
        
    	# Read the next line from the file
    	file_1_line = file_1.readline()
    	file_2_line = file_2.readline()
    
    file_1.close()
    file_2.close()
    return(True)


def check():

    try:
        exists = os.path.exists(FILE_STUD_PATH)
        assert exists == False
    except:
        sys.exit()
    
    result = fcmp(FILE_STUD_PATH, FILE_ANS_PATH)   
    assert result == True


def main():
    check()

if __name__ == "__main__":
    main()
