import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import feature


def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)

	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# return the edged image
	return edged

def median_Canny(image, thresh1, thresh2):
    median = np.median(image)
    image = cv2.Canny(image, int(thresh1 * median), int(thresh2 * median))
    return image


plt.ion()
i=0

vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()

else:
    rval = False


while i <1000:
    rval, frame = vc.read()
    origanial = frame
    blue, green, red = cv2.split(frame)
    blue_edges = median_Canny(blue, 0.2, 0.3)
    green_edges = median_Canny(green, 0.2, 0.3)
    red_edges = median_Canny(red, 0.2, 0.3)

    edges = blue_edges | green_edges | red_edges


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    wide = cv2.Canny(blurred, 10,200)
    tight = cv2.Canny(blurred, 225, 250)
    auto = auto_canny(blurred)
    auto = cv2.bitwise_not(auto)
    frame = auto

    image, contours, hierarchy = cv2.findContours(auto, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for c in contours:
        if cv2.contourArea(c) < 3000:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)

        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame,[box],0,(0,191,255),2)
		
    #magic end
    #frame[200:] = cv2.bitwise_not(frame[200:])
    plt.imshow(frame, cmap="hot") #auto)

    i+=1;
    plt.show()
    plt.pause(0.0001) #Note this correction
    plt.clf(); # cache clearing -->

#plt.imshow(edges1)
#plt.show()
