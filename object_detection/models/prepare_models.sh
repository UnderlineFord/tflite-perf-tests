#!/bin/bash

bash requirements_for_tflite_conversion.sh
bash tflite_conversion.sh ssd_mobilenet_v2 ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz
bash tflite_conversion.sh ssd_mobilenet_v1_fpn ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8.tar.gz
bash tflite_conversion.sh ssd_mobilenet_v2_fpnlite_320x320 ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz
bash tflite_conversion.sh ssd_mobilenet_v2_fpnlite_640x640 ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz