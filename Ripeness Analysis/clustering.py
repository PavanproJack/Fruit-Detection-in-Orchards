import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import glob


path = "/Users/pavankumar/Documents/Robotics MSc/Dissertation/Fruit-Detection-in-Orchards/Ripeness Analysis/msk_ripen"

os.chdir(path)

all_files = glob.glob("*")
imgList = []
for img in all_files:
    imgList.append(img)

print((imgList))

original_image = cv2.imread(imgList[0])
#original_image = cv2.imread("berry.jpg")
#print(original_image)

#original_image = io[170:230, 200:245]

img=cv2.cvtColor(original_image,cv2.COLOR_BGR2HSV)

vectorized = img.reshape((-1,3))

vectorized = np.float32(vectorized)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K = 2
attempts=10
ret,label,center=cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)

res = center[label.flatten()]
result_image = res.reshape((img.shape))

figure_size = 15 

plt.figure(figsize=(figure_size,figure_size))
plt.subplot(1,2,1),plt.imshow(original_image)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(result_image)
plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])
plt.show()


