import matplotlib.pyplot as plt
import numpy as np
import cv2

def find_points(list_bbox:list)->list:
  '''

  list_bbox: list of bboxes.
  exemple: Bounding box for object 2 "PAScarRear" (Xmin, Ymin) - (Xmax, Ymax) : (26, 37) - (53, 55)
  '''
  # CODE
  points = []
  for i in range(len(list_bbox)):
    bbox = list_bbox[i] # Get Bbox points
    start = bbox.find(':')+2
    bbox = bbox[start:]
    idx1 = bbox.find('(')+1
    idx2 = bbox.find(',',idx1)
    x1 = int(bbox[idx1:idx2])
    idx1 = idx2+2
    idx2 = bbox.find(')',idx1)
    y1 = int(bbox[idx1:idx2])
    start_point = (x1,y1)
    idx1 = idx2
    idx1 = bbox.find('(',idx1)+1
    idx2 = bbox.find(',',idx1)
    x2 = int(bbox[idx1:idx2])
    idx1 = idx2+2
    idx2 = bbox.find(')',idx1)
    y2 = int(bbox[idx1:idx2])
    end_point = (x2,y2)
    points.append((start_point,end_point))
  return points