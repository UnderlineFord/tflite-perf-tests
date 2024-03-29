#!/bin/bash

python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v3_small/model.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v3_large/model.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v2_fpnlite_640x640/method1.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v2_fpnlite_640x640/method3.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v2_fpnlite_320x320/method1.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v2_fpnlite_320x320/method3.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v2/method2.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v1_fpn/method1.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v1_fpn/method3.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v1_1_default/model.tflite
python3 object_detection_withoutGUI.py --model_path models/ssd_mobilenet_v1/model.tflite
python3 object_detection_withoutGUI.py --model_path models/mobilenetv2_danoorkans_ayya/model.tflite
python3 object_detection_withoutGUI.py --model_path models/mobile_object_localizer/model.tflite
