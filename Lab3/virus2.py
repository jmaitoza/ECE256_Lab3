#!/usr/bin/env python3
import glob, os, re

path = "/home/pi/sandbox" #sandboxes the virus to attack specific directory
os.chdir(path)
name = "MAngelou"
count = 1 
text = ".txt"
for files in glob.glob('*.txt'): #iterates through files with .txt 
    if re.match('maya.*\.txt', files):
        continue
    else:
        os.rename(files, "MAngelou" + str(count) + ".txt") #renames the file and turns the counter value into a string so it gets the correct value 
        count += 1

