import os
import time                        #4

print(os.getcwd())                 #1
metadata = os.stat('os_FileInfo.py')     #2
print(metadata.st_mtime)           #3

time.localtime(metadata.st_mtime)  #5
print(metadata.st_size)                              #1


