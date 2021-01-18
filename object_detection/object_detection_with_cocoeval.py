
import numpy as np
import cv2
import time
from fps import FPS
import os
import argparse
import random
import json


### below files should be there in the directory

from visualization_utils import draw_bounding_boxes_on_image_array
from utils import load_image
from detector import ObjectDetectorLite


parser = argparse.ArgumentParser(description='Object Detection')
parser.add_argument('--model_path', type=str, help='Specify the model path', default='models/detect.tflite')
parser.add_argument('--label_path', type=str, help='Specify the label map', default='models/default_setting/coco_labelmap.txt')
parser.add_argument('--image_path', type=str, help='Specify the image path', default='datasets/coco2014_val/images')

parser.add_argument('--n_bit', type=str, help='Specify 32/ 64 bit hardware', default=32)
parser.add_argument('--hardware', type=str, help='Specify hardware', default='rpi')


args = parser.parse_args()

model_path=args.model_path
label_path=args.label_path
image_path=args.image_path
n_bit=args.n_bit
hardware=args.hardware

model_name=model_path.strip().split('/')[-2]
method=model_path.strip().split('/')[-1][:-7]
model_name+='_'+method

resFile=f'results/{model_name}_res_{n_bit}bit_{hardware}_python.json'

##################################################

confidence=0.6
#init_waiting_time= int(input("input initial waiting time (seconds) : ")) 
init_waiting_time=0

my_fps=FPS()

images=[]
    images.append()
#images=np.array(images)
    
def pred_given_imgs(input_size):
    start=time.time()
    for img in sorted(os.listdir(image_path)):
        image = cv2.imread(image_path+'/'+img)
        
        if time.time()-start >init_waiting_time: # initial waiting time
            my_fps.start()
            image=cv2.resize(image, tuple(input_size))
            boxes, scores, classes = detector.detect(image, confidence)
            my_fps.stop()
        else:
            image=cv2.resize(image, tuple(input_size))
            boxes, scores, classes = detector.detect(image, confidence)
        #for label, score in zip(classes, scores):
        #    print(label, score)

        results_dict= {'boxes':boxes, 'scores':scores, 'classes':classes, 'image_id', img}
        with open(resFile, 'r') as f:
            json.dump(results_dict, resFile)
            
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
