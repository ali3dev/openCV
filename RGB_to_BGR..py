#import cv2, numpy and matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("ali.png")
#Displaying image using plt.imshow() method
plt.imshow(img) 

# save image (saveFileName,whichImgSave)
cv2.imwrite('path_to_output.jpg', img )


#hold the window
plt.waitforbuttonpress()
plt.close('all')




