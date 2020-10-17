import cv2 as cv
import numpy as np

def noop(x): return None

#### Object detection from image using HSV color space
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

while True:
    ## 2. Read and convert image to HSV color space
    image = cv.imread('paralect.png')
    imageHsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    ## 3. Get min and max HSV values from Set Mask window
    minHue = cv.getTrackbarPos("Min Hue", SET_MASK_WINDOW)
    maxHue = cv.getTrackbarPos("Max Hue", SET_MASK_WINDOW)
    minSat = cv.getTrackbarPos("Min Sat", SET_MASK_WINDOW)
    maxSat = cv.getTrackbarPos("Max Sat", SET_MASK_WINDOW)
    minVal = cv.getTrackbarPos("Min Val", SET_MASK_WINDOW)
    maxVal = cv.getTrackbarPos("Max Val", SET_MASK_WINDOW)
    minHsv = np.array([minHue, minSat, minVal])
    maxHsv = np.array([maxHue, maxSat, maxVal])

    ## 4. Create mask and result (masked) image
    # params: input array, lower boundary array, upper boundary array
    mask = cv.inRange(imageHsv, minHsv, maxHsv)
    # params: src1	array, src2 array, mask
    resultImage = cv.bitwise_and(image, image, mask=mask)

    ## 5. Show images
    cv.imshow("Input Image", image)
    # cv.imshow("Mask", mask)   # optional
    cv.imshow("Result Image", resultImage)
    if cv.waitKey(1) == 27: break   # Wait Esc key to end program