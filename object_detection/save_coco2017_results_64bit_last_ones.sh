#!/bin/bash

python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v1_fpn/method3.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False --n_bit=64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v1_1_default/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False --n_bit=64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v1/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False --n_bit=64
python3 object_detection_with_cocoeval.py --model_path models/mobilenetv2_danoorkans_ayya/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False --n_bit=64
python3 object_detection_with_cocoeval.py --model_path models/mobile_object_localizer/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False --n_bit=64