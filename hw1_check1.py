"""
Tests BAIS:6060 Homework 1
"""
from io import StringIO 
import filecmp
import os.path
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
        

def file1():

    try:
        exists = os.path.exists("lasers_small.csv")
        assert exists == True
    except:
        sys.exit()
    
    with Capturing() as output:  
        f1 = "lasers_small.csv"
        f2 = "a.csv"
        result = filecmp.cmp(f1, f2)
        print(result)

    assert output == ['True']

def main():
    file1()

if __name__ == "__main__":
    main()
