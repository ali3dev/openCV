# import cv2 as cv 

# # Try to load the image
# old_img = cv.imread('D:\\openCV\\ali.png')  # Update this path if necessary

# # Check if the image was loaded successfully
# if old_img is None:
#     print("Error: Unable to load image. Please check the file path.")
# else:
#     # Resize the image
#     old_img = cv.resize(old_img, (500, 700))

#     txt_img = cv.putText(
#     img = old_img,
#     text = 'Ali',
#     org = (60,25), # org 60 is height and 25 is increase going to bottom if alternative top 
#     fontFace = 2,
#     fontScale = 1,
#     color = (0,0,255),
#     thickness = 2,
#     lineType = 16,
#     bottomLeftOrigin = False)

#     # Define the top-left and bottom-right corners of the rectangle
#     top_left = (40, 30)
#     bottom_right = (400, 450)

#     # Draw the rectangle on the image
#     new_img = cv.rectangle( txt_img, top_left, bottom_right, color=(0, 255, 0), thickness=4)

#     # Display the image with the rectangle
#     cv.imshow('ali', new_img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()


