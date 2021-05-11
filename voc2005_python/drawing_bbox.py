import matplotlib.pyplot as plt
import numpy as np
import cv2
import pathlib
from dataset import dataset

path = pathlib.Path('../VOC2005_1/Annotations/Caltech_cars').iterdir()
path_list = list(path)

def drawing_bbox(bbox_list,img_list)->None:
  '''
  Image a drawing bounding box
  Make subplots depending on the number of images
  '''
  # CODE
  plt.figure(figsize=(7,2),dpi=200)
  for i,img in enumerate(img_list):
    for point in bbox_list[i]:
      start_point,end_point = point 
      cv2.rectangle(img,start_point,end_point,color=(255,0,0),thickness=1)
    plt.subplot(2,7,i+1)
    plt.imshow(img)
    plt.axis('off')
  plt.show()

bbox_list,img_list = dataset(path_list)
drawing_bbox(bbox_list,img_list)