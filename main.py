import matplotlib.pyplot as plt
import numpy as np
import cv2

filename = 'lasetti01'
f = open(f'labeling file/{filename}.txt').read().split(' ')
list1 = [float(i) for i in f][1:]

img = cv2.imread(f'car/{filename}.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

H,W = img.shape[:2]
x = int(list1[0]*W)
y = int(list1[1]*H)
w = int(list1[2]*W)
h = int(list1[3]*H)

cv2.rectangle(img,(x-w//2,y-h//2),(x+w//2,y+h//2),color=(255,0,0),thickness=1)
plt.imshow(img)
plt.show()