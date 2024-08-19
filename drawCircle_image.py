import cv2 as cv

img = cv.imread('ali.png')
old_img = cv.resize(img, (600, 800))

txt_img = cv.putText(
img = old_img,
text = 'Ali',
org = (500,200),
fontFace = 2,
fontScale = 1,
color = (0,255,0),
thickness = 3,
lineType = 16,
bottomLeftOrigin = False)

#draw circle 
new_img = cv.circle(img=txt_img,center=(260,250),radius=250,color=(0,255,0),thickness=2,lineType=12)
cv.imshow('ali',new_img)


key = cv.waitKey(0)  # Wait indefinitely for a key press
if key == ord('q'):
    print("Q key pressed")

cv.destroyAllWindows()