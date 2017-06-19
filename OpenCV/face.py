#!/opt/local/bin/python
import cv2
CAM_ID = 0

#Open the CAM
cap = cv2.VideoCapture(CAM_ID) #카메라 생성

#Check that the camera is opened
if cap.isOpened() == False: #카메라 생성 확인
    print( 'Can\'t open the CAM(%d)' % (CAM_ID))
    exit()

#create the window & change the window size
#윈도우 생성 및 사이즈 변경
cv2.namedWindow('Face')

face_cascade = cv2.CascadeClassifier()
face_cascade.load('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')


while(True):
    #read the camera image
    #카메라에서 이미지 얻기
    ret, frame = cap.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayframe = cv2.equalizeHist(grayframe)

    faces = face_cascade.detectMultiScale(grayframe, 1.1, 3, 0, (30, 30))
    """
    cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[,
                                           flags[, minSize[, maxSize]]]]]) → objects
    image 실제 이미지
    objects [반환값] 얼굴 검출 위치와 영역 변수
    scaleFactor 이미지 스케일
    minNeighbors 얼굴 검출 후보들의 갯수
    flags 이전 cascade와 동일하다 cvHaarDetectObjects 함수 에서
          새로운 cascade에서는 사용하지 않는다.
    minSize 가능한 최소 객체 사이즈
    maxSize 가능한 최대 객체 사이즈
    """
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3, 4, 0)
    """
    cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) → None
    img 적용할 이미지
    pt1 그릴 상자의 꼭지점
    pt2 pt1의 반대편 꼭지점
    color 상자의 색상
    thickness 상자의 라인들의 두께 음수 또는 CV_FILLED를 주면 상자를 채운다.
    lineType 라인의 모양 line()함수 확인하기
    shift ?? Number of fractional bits in the point coordinates.
    포인트 좌표의 분수 비트의 수??
    """

    cv2.imshow('Face',frame)

    #wait keyboard input until 10ms
    #10ms 동안 키입력 대기
    if cv2.waitKey(10) >= 0:
        break;

#close the window
#윈도우 종료
cap.release()
cv2.destroyWindow('Face')