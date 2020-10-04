import cv2

# videoCaptureObject = cv2.VideoCapture(0)
# while(True):
#     ret,frame = videoCaptureObject.read()
#     cv2.imshow('Capturing Video',frame)
#     if(cv2.waitKey(1) & 0xFF == ord('q')):
#         videoCaptureObject.release()
#         cv2.destroyAllWindows()


videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NonuPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()