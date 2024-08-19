import cv2 
import numpy as np 

vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read()
    cv2.imshow('frame', frame)
    b = frame[:,:, 0]
    g = frame[:,:, 1]
    r = frame[:,:, 2]

    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)
    # print(b_mean,g_mean,r_mean)
    
    total_mean = b_mean + g_mean + r_mean
    b_mean_norm = b_mean / total_mean
    g_mean_norm = g_mean / total_mean
    r_mean_norm = r_mean / total_mean

    # displaying the most prominent color
    if b_mean > g_mean and b_mean > r_mean:
        print("Blue")
    elif g_mean > r_mean and g_mean > b_mean:
        print("Green")
    else:
        print("Red")

    # breaking the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # releasing the video capture object and closing all windows
vid.release()
cv2.destroyAllWindows()
