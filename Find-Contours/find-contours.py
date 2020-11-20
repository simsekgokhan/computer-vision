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
print("Number of contours found: " + str(len(contours)))

## A contour: Numpy array of (x,y) - coordinates of the boundary of a shape
# print(contours[1]) # [ [[ 90 336]] [[ 91 335]] ... [[ 90 421]] ]

## Draw all (-1) contours 
##                             index, color, thickness
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
## Draw [1]st contour
# cv2.drawContours(img, contours, 1, (0, 255, 0), 3)
# cv2.drawContours(img, [contours[1]], 0, (0, 255, 0), 3)

cv2.imshow("--", img)
cv2.imshow("---", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()