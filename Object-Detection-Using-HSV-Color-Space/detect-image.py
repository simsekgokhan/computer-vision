import cv2
import numpy as np

def noop(x): return None

#### Object detection from image using HSV color space
#### (HSV -> Hue, Saturation, Value)

## 1. Create "Set Mask" window with default HSV range to detect blue color
SET_MASK_WINDOW = "Set Mask"
cv2.namedWindow(SET_MASK_WINDOW)
cv2.createTrackbar("Min Hue", SET_MASK_WINDOW, 90, 179, noop)
cv2.createTrackbar("Max Hue", SET_MASK_WINDOW, 140, 179, noop)
cv2.createTrackbar("Min Sat", SET_MASK_WINDOW, 74, 255, noop)
cv2.createTrackbar("Max Sat", SET_MASK_WINDOW, 255, 255, noop)
cv2.createTrackbar("Min Val", SET_MASK_WINDOW, 0, 255, noop)
cv2.createTrackbar("Max Val", SET_MASK_WINDOW, 255, 255, noop)

while True:
    ## 2. Read and convert image to HSV color space
    image = cv2.imread('paralect.png')
    imageHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    ## 3. Get min and max HSV values from Set Mask window
    minHue = cv2.getTrackbarPos("Min Hue", SET_MASK_WINDOW)
    maxHue = cv2.getTrackbarPos("Max Hue", SET_MASK_WINDOW)
    minSat = cv2.getTrackbarPos("Min Sat", SET_MASK_WINDOW)
    maxSat = cv2.getTrackbarPos("Max Sat", SET_MASK_WINDOW)
    minVal = cv2.getTrackbarPos("Min Val", SET_MASK_WINDOW)
    maxVal = cv2.getTrackbarPos("Max Val", SET_MASK_WINDOW)
    minHsv = np.array([minHue, minSat, minVal])
    maxHsv = np.array([maxHue, maxSat, maxVal])

    ## 4. Create mask and result (masked) image
    mask = cv2.inRange(imageHsv, minHsv, maxHsv)
    resultImage = cv2.bitwise_and(image, image, mask=mask)

    ## 5. Show images
    cv2.imshow("Input Image", image)
    # cv2.imshow("Mask", mask)
    cv2.imshow("Result Image", resultImage)
    # ---
    key = cv2.waitKey(1)
    if key == 27: break

cv2.destroyAllWindows()