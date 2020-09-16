import cv2
import numpy as np

def noop(x): return None

#### Object detection from video using HSV color space
#### (HSV -> Hue, Saturation, Value)

## 1. Create "Set Mask" window with default HSV range to detect blue color
SET_MASK_WINDOW = "Set Mask"
cv2.namedWindow(SET_MASK_WINDOW)
cv2.createTrackbar("Min Hue", SET_MASK_WINDOW, 90, 255, noop)
cv2.createTrackbar("Max Hue", SET_MASK_WINDOW, 140, 255, noop)
cv2.createTrackbar("Min Sat", SET_MASK_WINDOW, 74, 255, noop)
cv2.createTrackbar("Max Sat", SET_MASK_WINDOW, 255, 255, noop)
cv2.createTrackbar("Min Val", SET_MASK_WINDOW, 0, 255, noop)
cv2.createTrackbar("Max Val", SET_MASK_WINDOW, 255, 255, noop)

## 2. Capture from default camera
videoCapture = cv2.VideoCapture(0)

while True:
    ## 3. Capture video from camera and convert to HSV color space
    _, capturedVideo = videoCapture.read() # video
    # rotate video 180 degrees (it starts upside down on Windows)
    capturedVideo = cv2.flip(capturedVideo, -1)
    capturedVideoHsv = cv2.cvtColor(capturedVideo, cv2.COLOR_BGR2HSV)

    ## 4. Get min and max HSV values from Set Mask window
    minHue = cv2.getTrackbarPos("Min Hue", SET_MASK_WINDOW)
    maxHue = cv2.getTrackbarPos("Max Hue", SET_MASK_WINDOW)
    minSat = cv2.getTrackbarPos("Min Sat", SET_MASK_WINDOW)
    maxSat = cv2.getTrackbarPos("Max Sat", SET_MASK_WINDOW)
    minVal = cv2.getTrackbarPos("Min Val", SET_MASK_WINDOW)
    maxVal = cv2.getTrackbarPos("Max Val", SET_MASK_WINDOW)
    minHsv = np.array([minHue, minSat, minVal])
    maxHsv = np.array([maxHue, maxSat, maxVal])

    ## 5. Create mask and result (masked) video
    mask = cv2.inRange(capturedVideoHsv, minHsv, maxHsv)
    resultVideo = cv2.bitwise_and(capturedVideo, capturedVideo, mask=mask)

    ## 6. Show videos
    cv2.imshow("Captured Video", capturedVideo)
    # cv2.imshow("Mask", mask)
    cv2.imshow("Result (Masked) Video", resultVideo)
    # ---
    key = cv2.waitKey(1)
    if key == 27: break

videoCapture.release()
cv2.destroyAllWindows()