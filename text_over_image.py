import cv2 as cv 

img_get = cv.imread('D:\\openCV\\ali.png')
img_get = cv.resize(img_get,(500,600))



txt = cv.putText(
img = img_get,
text = 'ali',
org = (50,80),
fontFace = cv.FONT_HERSHEY_DUPLEX,
fontScale = 3,
color = (0,0,255),
thickness = 3,
lineType = cv.LINE_8,
bottomLeftOrigin = False
)

cv.imshow('ali', img_get)
cv.waitKey(0)
cv.destroyAllWindows()

