import numpy as np
import cv2

img = cv2.imread('shapes.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("-", img)

## For better accuracy, use binary images
## ret: the threshold used, thres: thresholded image
thres_setting = 220  # set custom per image
ret, thresh = cv2.threshold(imgGrey, thres_setting, 255, cv2.THRESH_BINARY)

## Params: Source image, contour retrieval mode, contour approximation method
##         (InputArray	image, int	mode, int	method, Point	offset = Point())
## Ret   : OutputArrayOfArrays contours, OutputArray	hierarchy
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  ## cv.CHAIN_APPROX_NONE  : save all the boundary points 
  ## cv.CHAIN_APPROX_SIMPLE: remove all redundant points, compresses 
  ##                         the contour, thereby saving memory.
print("Number of contours found:", len(contours))

for contour in contours:
    ### --- 1. Draw around contours
    ## approxPolyDP(): Approximate a polygonal curve with specified precision
    ## epsilon: approximation accuracy. maximum distance between the original 
    ##          curve and its approximation.
    ## arcLength(): curve length
    approx = cv2.approxPolyDP(curve=contour, 
      epsilon=0.01*cv2.arcLength(curve=contour, closed=True), closed=True)
    black = (0,0,0)
    cv2.drawContours(img, contours=[approx], contourIdx=0, color=black, thickness=5)

    # print("---", approx)  ## for tri: [[[320 313]] [[382 422]] [[257 419]]]

    ### --- 2. Put text
    ## ravel(): return contiguous flattened array
    x = approx.ravel()[0] - 20
    y = approx.ravel()[1] - 10    
    points = len(approx) # number of points/curves
    font = cv2.FONT_HERSHEY_COMPLEX    
    fontScale = 0.7
    if points == 3:
        cv2.putText(img, "Triangle", (x, y), font, fontScale, black)
    elif points == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspRatio = float(w)/h # aspect ratio
        str = "Square" if (aspRatio >= 0.95 and aspRatio <= 1.05) else "Rectangle"
        cv2.putText(img, str, (x, y), font, fontScale, black)
    elif points == 5:
        cv2.putText(img, "Pentagon", (x, y), font, fontScale, black)
    elif points == 10:
        cv2.putText(img, "Star", (x, y), font, fontScale, black)
    else:
        cv2.putText(img, "Circle", (x, y), font, fontScale, black)
        

cv2.imshow("--", img)
cv2.imshow("---", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()