# Model details

* model name : ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8
* downloaded from : [tf2 zoo](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection)

# Result comparison between different optimization schemes

**Optimization schemes**|**dataset**|**dtype**|**input shape**|**detection period (sec)**|**FPS (CPU)**|**FPS (RPI)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Dynamic|coco|float32|640|20|0.0353|0.4991
Convert-only|coco|float32|640|20|1.1954|**0.7038**


