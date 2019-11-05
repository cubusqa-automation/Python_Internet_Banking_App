
import os
import sys


def test_get_pypath():
    myPath = sys.path.insert(0, os.path.join(os.getcwd(), '..', '..', '..'))
    print("---My Py Path---", myPath)
