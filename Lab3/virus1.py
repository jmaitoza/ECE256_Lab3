#!/usr/bin/env python3
import glob, os, re
mayatext = open('maya.txt', 'r')
path = "/home/pi/sandbox"
os.chdir(path)
#mayatext = open('maya.txt', 'r')
maya = mayatext.read()

for files in glob.glob('*.txt'):
    if re.match('maya.*\.txt', files):
        continue
    else:
        with open(files, 'w') as f:
            f.write(maya)

mayatext.close()











    
