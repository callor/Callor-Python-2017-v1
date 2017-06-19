'''
Created on 2017. 6. 19.

@author: callor
'''
# 파일 관련 기능을 사용하기 위해 os 플러그인 import
import os

# 파일 복사 유틸리티 import
import shutil

# 파일 복사 함수 선언
def search(sdirname,tdirname):
    # 지정된 소스 폴더의 파일들을 읽어서 filenames 변수에 리스트로 저장
    filenames = os.listdir(sdirname)
    
    # 저장된 리스트를 순회하면서
    for filename in filenames:
        
        # java 라는 문자열이 포함된 이름이 있는가?
        if "java" in filename:
            
            # 있으면 target 폴더에 복사
            shutil.copy(sdirname + filename,tdirname)
            print("파일복사 "  + filename)


# search 함수를 호출하기 전 원본 폴더와 복사본 폴더를 변수에 할당
sourcePath = "C:/test1/"
targetPath = "C:/test2/"

# 원본 폴더이름과 복사본 폴더 이름을 search에 매개변수로 넘겨서 실행
search(sourcePath,targetPath)