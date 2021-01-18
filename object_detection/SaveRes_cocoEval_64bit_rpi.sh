#!/bin/bash

python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v3_small/model.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v3_large/model.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v2_fpnlite_640x640/method1.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v2_fpnlite_640x640/method3.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v2_fpnlite_320x320/method1.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v2_fpnlite_320x320/method3.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v2/method2.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v1_fpn/method1.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v1_fpn/method3.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v1_1_default/model.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v1/model.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/mobilenetv2_danoorkans_ayya/model.tflite --n_bit 64
python3 object_detection_with_cocoeval.py --model_path models/mobile_object_localizer/model.tflite --n_bit 64



