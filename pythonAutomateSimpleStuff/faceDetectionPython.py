import cv2
import sys
import os


print("t1")
cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
cascPath = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(cascPath)
print("t2")

video_capture = cv2.VideoCapture(0)
print("t")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=6,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()