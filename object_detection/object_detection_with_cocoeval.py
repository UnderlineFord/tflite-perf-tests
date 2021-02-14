
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
from detector_for_cocoeval import ObjectDetectorLite


parser = argparse.ArgumentParser(description='Object Detection')
parser.add_argument('--model_path', type=str, help='Specify the model path', default='models/detect.tflite')
parser.add_argument('--label_path', type=str, help='Specify the label map', default='models/default_setting/coco_labelmap.txt')
parser.add_argument('--image_path', type=str, help='Specify the image path', default='datasets/coco2014_val/images')
parser.add_argument('--save_results', type=str, help='Specify whether class index should be returned', default='False')

parser.add_argument('--n_bit', type=str, help='Specify 32/ 64 bit hardware', default=32)
parser.add_argument('--hardware', type=str, help='Specify hardware', default='rpi')
parser.add_argument('--coco_dataset_version', type=str, help='Specify coco version', default='2017')
parser.add_argument('--is_baseline', type=str, help='Specify coco version', default='True')
parser.add_argument('--is_checking_code', type=str, help='Specify coco version', default='False') # to check whether the code os correct


args = parser.parse_args()

model_path=args.model_path
label_path=args.label_path
image_path=args.image_path
return_classes=args.save_results
n_bit=args.n_bit
hardware=args.hardware
coco_dataset_version= args.coco_dataset_version
is_baseline=args.is_baseline
is_checking_code=args.is_checking_code

if return_classes=='True':return_classes=True
else:return_classes=False

model_name=model_path.strip().split('/')[-2]
method=model_path.strip().split('/')[-1][:-7]
model_name+='_'+method

os.makedirs(f'results/coco{coco_dataset_version}_val', exist_ok = True) 

if is_baseline=='True':
  resFile=f'results/coco{coco_dataset_version}_val/{model_name}@baseline.json'
else:
  resFile=f'results/coco{coco_dataset_version}_val/{model_name}@{n_bit}bit@{hardware}@python@results.json'


##################################################

confidence=0.5 #CHANGES RECENTLY
#init_waiting_time= int(input("input initial waiting time (seconds) : ")) 
init_waiting_time=0


def img_name2id(image_name_string, coco_dataset_version='2017'):
  if coco_dataset_version=='2017':
    return int(image_name_string.split('.')[0])
  elif coco_dataset_version=='2014':
    return int(image_name_string.split('.')[0][13:])

def get_bbox(box, original_img_size):
  '''
  below: from original annotation: bbox processing from https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/coco.py  
  [bbox_x, bbox_y, bbox_w, bbox_h] = ann['bbox']
  poly = [[bbox_x, bbox_y], [bbox_x, bbox_y+bbox_h], [bbox_x+bbox_w, bbox_y+bbox_h], [bbox_x+bbox_w, bbox_y]]
  '''

  ymin,xmin,ymax,xmax = box
  im_height, im_width = original_img_size  ## original image size should come here !!! ## NOTE THAT -> HEIGHT COMES FIRST
  (left, right, top, bottom) = (xmin * im_width, xmax * im_width, ymin * im_height, ymax * im_height)
  
  width=right-left
  height=bottom-top

  return [xmin * im_width, ymin * im_height, width, height] #obtained carefully. If change/ replace this -> please double check

  #return [xmin*10, ymin*10, (xmax- xmin)*10, (ymax- ymin)*10]
  #return [(xmin +xmax)* im_width/2, (ymin+ymax) * im_height/2, width, height]

  #return [0,0, 100, 300]

def pred_given_imgs(input_size, return_classes=False, coco_dataset_version='2017'):
    my_fps=FPS()

    results = []
    if is_checking_code=='True':
      img_list=sorted(os.listdir(image_path))[:100]
    else:img_list=sorted(os.listdir(image_path))
    for i in range(len(img_list)):
        if i%100==0:print(f'image number : {i}/{len(img_list)}')
        img= img_list[i]
        image = cv2.imread(image_path+'/'+img)
        original_img_size = image.shape[:2]

        if return_classes==True:
          (details, my_fps) = detector.detect(image, confidence, input_size, return_classes=return_classes, my_fps=my_fps)
          (boxes, scores, classes, cat_ids)=details
        else:
          (details, my_fps)= detector.detect(image, confidence, input_size, return_classes=return_classes, my_fps=my_fps)
          (boxes, scores, classes)=details

        #print(my_fps.elapsed_time_list)

        for j in range(len(boxes)):
          bbox= get_bbox(boxes[j], original_img_size)

          if return_classes:cat_id = int(cat_ids[j])
          else:cat_id=classes[j]
          results.append({'bbox': bbox,'category_id': cat_id, 'image_id': img_name2id(img, coco_dataset_version), 'score': scores[j].astype('float')})

          #for k in range(len(annot_data['annotations'])):
          #  if annot_data['annotations'][k]['image_id']==img_name2id(img):
          #    results.append({'bbox': annot_data['annotations'][k]['bbox'],'category_id': annot_data['annotations'][k]['category_id'], 'image_id': img_name2id(img), 'score': 1.0})

    with open(resFile, 'w') as f:
      json.dump(results, f)
    print('results File : ',resFile)
    print('fps : ', my_fps.get_fps(), detector.get_input_size())


#annotFile = 'datasets/coco2017_val/instances_val2017.json'
#with open(annotFile) as f:
#  annot_data= json.load(f)

detector=ObjectDetectorLite(model_path=model_path, label_path=label_path)
input_size= detector.get_input_size()
pred_given_imgs(input_size, return_classes=return_classes, coco_dataset_version= coco_dataset_version)

detector.close()
