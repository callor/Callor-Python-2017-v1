import os                                            #1
print(os.getcwd())                                   #2
os.chdir('/Users/callor/Documents/2017년/work2017/HelloPython/com.callor.webCrolling')  #3
print(os.getcwd())                                   #4

print(os.path.join('/Users/callor/Documents/2017년/work2017/HelloPython/com.callor.webCrolling', 'humansize.py'))              #1
print(os.path.join('/Users/callor/Documents/2017년/work2017/HelloPython/com.callor.webCrolling', 'humansize.py'))               #2
print(os.path.expanduser('~'))                                                               #3
print(os.path.join(os.path.expanduser('~'), 'diveintopython3', 'examples', 'humansize.py'))  #4
