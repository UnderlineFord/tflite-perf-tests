# Model details

* model name : ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8
* downloaded from : [tf2 zoo](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection)
* methods used : 1, 3

# Result comparison between different methods

**Method**|**dataset**|**dtype**|**input shape**|**detection period (sec)**|**FPS (CPU)**|**FPS (RPI)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
method1|coco|float32|640|20|0.0353|0.4991
method3|coco|float32|640|20|1.1954|**0.7038**


