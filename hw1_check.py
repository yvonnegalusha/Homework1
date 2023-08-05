"""
Tests BAIS:6060 Homework 1
"""

import filecmp
import os.path
import sys

def file1():

    try:
        exists = os.path.exists("lasers_small.csv")
	assert exists == True
    except:
        sys.exit()

    f1 = "lasers_small.csv"
    f2 = "a.csv"
    result = filecmp.cmp(f1, f2, shallow=False)
    
    assert result == TRUE

def main():
    file1()

if __name__ = "__main__":
    main()
