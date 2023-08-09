"""
Tests BAIS:6060 Homework 1 Answers
"""

import os.path
import sys

        
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
        exists = os.path.exists("output.txt")
        assert exists == True
    except:
        sys.exit()
    
    result = fcmp("output.txt", "a.txt")   
    assert result == True


def main():
    check()

if __name__ == "__main__":
    main()
