# Write a Python program to get the Python version you are using
import os
import sys
class Version():
    def __init__(self):
        pass
    def print_python_version(self):
        print(sys.version)
        print(os.system('python --version'))

version = Version()
version.print_python_version()