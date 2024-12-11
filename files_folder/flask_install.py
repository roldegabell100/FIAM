import subprocess
import os
from folders import *
from files import *


# Flask installation commends
os.chdir(path)
subprocess.call(['pip3', 'install', 'pipenv'])
subprocess.call(['pipenv', 'install', 'flask'])
subprocess.call(['python3', '-m', 'pipenv'])
subprocess.call(['pipenv', 'shell'])