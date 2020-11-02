#!/usr/bin/env python3
import glob, os, re

path = "/home/pi/sandbox"
os.chdir(path)
name = "MAngelou"
count = 1
text = ".txt"
for files in glob.glob('*.txt'):
    if re.match('maya.*\.txt', files):
        continue
    else:
        os.rename(files, "MAngelou" + str(count) + ".txt")
        count += 1

