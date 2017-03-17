import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
import scipy
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

vc = cv2.VideoCapture(0)

if vc.isOpened():
	rval, frame = vc.read()
	scipy.misc.imsave('input.jpg',frame)
	
else:
    rval = False
