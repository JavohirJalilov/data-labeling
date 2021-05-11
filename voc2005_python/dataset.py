import matplotlib.pyplot as plt
import numpy as np
import cv2
import pathlib
from find_points import find_points

path = pathlib.Path('../VOC2005_1/Annotations/Caltech_cars').iterdir()
path_list = list(path)

def dataset(path_list:list):
  '''
  return points to lists
  return the images to the lists
  '''
  bbox_list = []
  img_list = []
  # CODE
  for file_path in path_list:
    f = open(file_path).read().split('\n')
    # find the file path and bbox points and place them in the list
    list_data = [i for i in f if 'Image filename' in i or 'Bounding box for object' in i]
    img_path = list_data.pop(0) # The path to the file in index 0
    idx1 = img_path.find('"')+1
    idx2 = img_path.find('"',idx1)
    img_path = img_path[idx1:idx2]
    img = cv2.imread(img_path)
    try:
      img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
      img_list.append(img)
      bbox_list.append(find_points(list_data))
    except:
      continue
  return bbox_list,img_list