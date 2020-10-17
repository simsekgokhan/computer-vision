import cv2 as cv
import numpy as np

def noop(x): return None

#### Object detection from video using HSV color space
#### (HSV -> Hue, Saturation, Value)

## 1. Create "Set Mask" window with default HSV range to detect blue color
SET_MASK_WINDOW = "Set Mask"
cv.namedWindow(SET_MASK_WINDOW, cv.WINDOW_NORMAL)
cv.createTrackbar("Min Hue", SET_MASK_WINDOW, 90, 179, noop)
cv.createTrackbar("Max Hue", SET_MASK_WINDOW, 140, 179, noop)
cv.createTrackbar("Min Sat", SET_MASK_WINDOW, 74, 255, noop)
cv.createTrackbar("Max Sat", SET_MASK_WINDOW, 255, 255, noop)
cv.createTrackbar("Min Val", SET_MASK_WINDOW, 0, 255, noop)
cv.createTrackbar("Max Val", SET_MASK_WINDOW, 255, 255, noop)

## 2. Capture from default camera
videoCapture = cv.VideoCapture(0)

while True:
    ## 3. Capture video from camera and convert to HSV color space
    _, capturedVideo = videoCapture.read() # video
    # rotate video 180 degrees (it starts upside down on Windows)
    # capturedVideo = cv.flip(capturedVideo, 1) # Win                                
    capturedVideo = cv.resize(capturedVideo, None, None, fx=0.5, fy=0.5) # macOS
    capturedVideoHsv = cv.cvtColor(capturedVideo, cv.COLOR_BGR2HSV)

    ## 4. Get min and max HSV values from Set Mask window
    minHue = cv.getTrackbarPos("Min Hue", SET_MASK_WINDOW)
    maxHue = cv.getTrackbarPos("Max Hue", SET_MASK_WINDOW)
    minSat = cv.getTrackbarPos("Min Sat", SET_MASK_WINDOW)
    maxSat = cv.getTrackbarPos("Max Sat", SET_MASK_WINDOW)
    minVal = cv.getTrackbarPos("Min Val", SET_MASK_WINDOW)
    maxVal = cv.getTrackbarPos("Max Val", SET_MASK_WINDOW)
    minHsv = np.array([minHue, minSat, minVal])
    maxHsv = np.array([maxHue, maxSat, maxVal])

    ## 5. Create mask and result (masked) video
    # params: input array, lower boundary array, upper boundary array
    mask = cv.inRange(capturedVideoHsv, minHsv, maxHsv)
    # params: src1	array, src2 array, mask
    resultVideo = cv.bitwise_and(capturedVideo, capturedVideo, mask=mask)

    ## 6. Show videos
    cv.imshow("Captured Video", capturedVideo)
    # cv.imshow("Mask", mask)  // optional
    cv.imshow("Result (Masked) Video", resultVideo)
    if cv.waitKey(1) == 27: break   # Wait Esc key to end program