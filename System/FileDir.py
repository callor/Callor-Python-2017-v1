'''
Created on 2017. 6. 19.

@author: callor
'''
import os
import shutil


def search(sdirname,tdirname):
    filenames = os.listdir(sdirname)
    for filename in filenames:
        if "java" in filename:
            shutil.copy(sdirname + filename,tdirname)
            print("파일복사 "  + filename)


sourcePath = "C:/test1/"
targetPath = "C:/test2/"
search(sourcePath,targetPath)