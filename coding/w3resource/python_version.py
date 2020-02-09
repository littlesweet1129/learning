import os
import sys
def python_version():
    print(sys.version)
    print(os.system('python --version'))

python_version()