import numpy 
import cv2
import os

mode = "test"
directory = "HandRecognition/"+mode+"/"
cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    frame  = cv2.flip(frame, 1)
    count = { 'zero':len(os.listdir(directory+"/0")),
               'one':len(os.listdir(directory+"/1")),
               'two':len(os.listdir(directory+"2")),
               'three': len(os.listdir(directory+"3")),
               'four':len(os.listdir(directory+"4")),
               'five':len(os.listdir(directory+"5"))}
    cv2.putText(frame, "mode:"+mode, (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 3)
    cv2.putText(frame, "Image Count", (10, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 3)
    cv2.putText(frame, "zero:"+str(count['zero']), (10, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 3)
    cv2.putText(frame, "one:"+str(count['one']), (10, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 3)
    cv2.putText(frame, "two:"+str(count['two']), (10, 140), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 3)
    cv2.putText(frame, "three:"+str(count['three']), (10, 160), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 3)
    cv2.putText(frame, "four:"+str(count['four']), (10, 180), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 3)
    cv2.putText(frame, "five:"+str(count['five']), (10, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 3)
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (128, 128)) 
    cv2.imshow("Frame", frame)
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    #_,roi = cv2.threshold(roi, 80,255,cv2.THRESH_BINARY)
    cv2.imshow('ROI',roi)
    interrupt  = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break 
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory +'/0/'+str(count['zero'])+'.jpg',roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory +'/1/'+str(count['one'])+'.jpg',roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory +'/2/'+str(count['two'])+'.jpg',roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory +'/3/'+str(count['three'])+'.jpg',roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory +'/4/'+str(count['four'])+'.jpg',roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory +'/5/'+str(count['five'])+'.jpg',roi)


cap.release()
cv2.destroyAllWindows()
    