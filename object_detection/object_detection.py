
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cv2
import time
from fps import FPS
import os
import argparse
import random


### below files should be there in the directory

from visualization_utils import draw_bounding_boxes_on_image_array
from utils import load_image
from detector import ObjectDetectorLite


parser = argparse.ArgumentParser(description='Object Detection')
parser.add_argument('--model_path', type=str, help='Specify the model path', default='models/ssd_mobilenet_v2_fpnlite_320x320/method5.tflite')
parser.add_argument('--label_path', type=str, help='Specify the label map', default='models/default_setting/coco_labelmap.txt')
parser.add_argument('--image_path', type=str, help='Specify the image path', default='sample_images')


args = parser.parse_args()

model_path=args.model_path
label_path=args.label_path
image_path=args.image_path


##################################################

confidence=0.6


my_fps=FPS()

images=[]
for img in sorted(os.listdir(image_path)):
    images.append(cv2.imread(image_path+'/'+img))
#images=np.array(images)
    
def pred_given_imgs(input_size):
    start=time.time()
    while(True):
        if time.time()-start>20:
            break
            
        image = random.choice(images)
        my_fps.start()
        image=cv2.resize(image, tuple(input_size))
        boxes, scores, classes = detector.detect(image, confidence)
        my_fps.stop()
        #for label, score in zip(classes, scores):
        #    print(label, score)
            
        if len(boxes) > 0:
            draw_bounding_boxes_on_image_array(image, boxes, display_str_list=classes)

        cv2.imshow('frame',image)
        
        
        
        
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    print('fps : ', my_fps.get_fps(), detector.get_input_size())
            
    cv2.destroyAllWindows()
     

detector=ObjectDetectorLite(model_path=model_path, label_path=label_path)
input_size= detector.get_input_size()
pred_given_imgs(input_size)

detector.close()
