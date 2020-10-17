import cv2 as cv

### 1. Load Haar feature-based cascade classifiers 
faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

### 2. Capture from video file
video = cv.VideoCapture('para.mp4')
while video.isOpened():
    ## Read video frames and convert to grayscale
    _, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    ### 3. Find areas with faces using Haar cascade classifier
    faces = faceCascade.detectMultiScale(image= gray, scaleFactor= 1.1, minNeighbors= 4)
        # scaleFactor: how much the image size is reduced at each image scale
        # minNeighbors: how many neighbors each candidate rectangle should have to retain it

    # x, y coordinates, w (weight) and h (height) of each "face" rectangle in frame
    for (x, y, w, h) in faces:
        # input, point1, point2, color, thickness=2    
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Get the region of interest: face rectangle sub-image in gray and colored
        faceROIGray = gray[y: y+h, x: x+w]
        faceROIColored = frame[y: y+h, x: x+w]    
        
        ### 4. Find areas with eyes in faces using Haar cascade classifier
        eyes = eyeCascade.detectMultiScale(faceROIGray)
        # x, y coordinates, w (weight) and h (height) of each "eye" rectangle in a face
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(faceROIColored, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    #### 5. Show the output video
    cv.imshow('Face Detection - OpenCV', frame)
    if cv.waitKey(10) == 27: break

video.release()
