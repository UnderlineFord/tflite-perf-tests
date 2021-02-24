#!/bin/bash

python3 object_detection.py --model_path models/ssd_mobilenet_v3_small/model.tflite 
python3 object_detection.py --model_path models/ssd_mobilenet_v3_large/model.tflite 
python3 object_detection.py --model_path models/ssd_mobilenet_v2/method2.tflite
python3 object_detection.py --model_path models/ssd_mobilenet_v1_1_default/model.tflite
