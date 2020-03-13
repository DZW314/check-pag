import os
import shutil
import sys
import time

import subprocess
from subprocess import *

# Steps
# 1. Copy the file "0supslist.bat" to the UXSP folders.
# 2. Run 0supslist.bat in the UXSP folders, that the 0supslist.txt is created.
#    Then rename 0supslist.txt (Use the folder's name).
# 3. Delete 0supslist.bat in the UXSP folder, and move the newly created file to ../ .
# The end.
bat = '0supslist.bat'
txt = '0supslist.txt'
# Step 1
for filename in next(os.walk("./"))[1]:
    shutil.copy(bat, filename)
    shutil.copy(txt, filename)
#os.system('E:\me\\05-uxsp\\11\\'+ bat)
for filename in next(os.walk("./"))[1]:
    os.chdir(sys.path[0] + '\\' + filename)
    os.system(bat)
#    subprocess.Popen('E:\me\\05-uxsp\\11\\'+ bat)

# Step 2

