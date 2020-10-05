import cv2 as cv

# Load Haar cascade classifiers
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# Capture from video file
video = cv.VideoCapture('paralect.mp4')
while video.isOpened():
    ## Read video frames and convert to grayscale
    _, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    ## Find faces using Haar cascade classifier
    faces = face_cascade.detectMultiScale(image= gray, scaleFactor= 1.1, minNeighbors= 4)
        # scaleFactor: how much the image size is reduced at each image scale
        # minNeighbors: how many neighbors each candidate rectangle should have to retain it

    # x, y coordinates, w (weight) and h (height) of each "face" rectangle in frame
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Get the region of interest: face rectangle sub-image in gray and colored
        roi_gray = gray[y: y+h, x: x+w]
        roi_colored = frame[y: y+h, x: x+w]    
        ## Find eyes using Haar cascade classifier
        eyes = eye_cascade.detectMultiScale(roi_gray)
        # x, y coordinates, w (weight) and h (height) of each "eye" rectangle in a face
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_colored, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    ## Show the output
    cv.imshow('Video', frame)
    if cv.waitKey(10) == 27: break

video.release()
