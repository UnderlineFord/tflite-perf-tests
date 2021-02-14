#!/bin/bash

python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v3_small/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v3_large/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v2/method2.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v1_1_default/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False
