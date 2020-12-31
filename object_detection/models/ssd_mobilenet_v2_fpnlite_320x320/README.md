# Model details

* model name : ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8
* downloaded from : [tf2 zoo](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection)

# Result comparison between different optimization schemes

**Optimization schemes**|**dataset**|**dtype**|**input shape**|**detection period (sec)**|**FPS (CPU)**|**FPS (RPI)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Dynamic|coco|float32|320|20|0.145|2.03
Convert-only|coco|float32|640|20|4.5612|**2.4678**


