
# Python 2/3 compatibility
from __future__ import print_function
import cv2 # Import the OpenCV library
import numpy as np # Import Numpy library
import matplotlib.pyplot as plt # Import matplotlib functionality
import sys # Enables the passing of arguments
from common import Sketcher
import glob
import os

# Project: Image Masking Using OpenCV
# Author: Addison Sears-Collins
# Date created: 9/18/2019
# Python version: 3.7
# Description: This program allows users to highlight a specific 
# object within an image by masking it.

# Define the file name of the image
'''INPUT_IMAGE = "fruits.jpg"
IMAGE_NAME = INPUT_IMAGE[:INPUT_IMAGE.index(".")]
OUTPUT_IMAGE = IMAGE_NAME + "_output.jpg"
TABLE_IMAGE = IMAGE_NAME + "_table.jpg"'''
 
os.chdir("/Users/pavankumar/Documents/Processed Datasets/scripts/UnRipe/")
print(os.getcwd())
all_files = glob.glob("*.jpg")
def main():
    """
    Main method of the program.
    """
    imgList = []
    for img in all_files:
        imgList.append(img)
    print(len(imgList))
    INPUT_IMAGE = imgList[14]
    IMAGE_NAME = INPUT_IMAGE[:INPUT_IMAGE.index(".")]
    OUTPUT_IMAGE = IMAGE_NAME + "_output.png"
    
    try:
        fn = sys.argv[1]
    except:
        fn = INPUT_IMAGE
    image = cv2.imread(INPUT_IMAGE)
    #cv2.imshow('Mask', image)
    #print(img)
    if image is None:
        print('Failed to load image file:', fn)
        sys.exit(1)
    # Create an image for sketching the mask
    image_mark = image.copy()
    sketch = Sketcher('Image', [image_mark], lambda : ((255, 255, 255), 255))
    while True:
        ch = cv2.waitKey()
        if ch == 27: # ESC - exit
            cv2.destroyAllWindows()
            break
        if ch == ord('r'): # r - mask the image
            break
        if ch == ord(' '): # SPACE - reset the inpainting mask
            image_mark[:] = image
            sketch.show()
    
    # define range of white color in HSV
    lower_white = np.array([0,0,255])
    upper_white = np.array([255,255,255])
    
    # Create the mask
    mask = cv2.inRange(image_mark, lower_white, upper_white)
    
    # Create the inverted mask
    mask_inv = cv2.bitwise_not(mask)

    # Convert to grayscale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract the dimensions of the original image
    rows, cols, channels = image.shape
    #print(image.shape)
    image = image[0:rows, 0:cols]
    # Bitwise-OR mask and original image
    colored_portion = cv2.bitwise_or(image, image, mask = mask)
    colored_portion = colored_portion[0:rows, 0:cols]
    os.chdir("/Users/pavankumar/Documents/Processed Datasets/scripts/msk_unripen/")
    #out = os.path.join(os.getcwd() , '/MaskedImages/').join(OUTPUT_IMAGE)
    print(OUTPUT_IMAGE)
    cv2.imwrite(OUTPUT_IMAGE, colored_portion)
    cv2.waitKey(0) # Wait for a keyboard event

if __name__ == '__main__':
    print(__doc__)
    main()
    cv2.destroyAllWindows()