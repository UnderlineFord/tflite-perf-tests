# Model details

* model name : ssd_mobilenet_v2_320x320_coco17_tpu-8
* downloaded from : [tf2 zoo](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection)
* optimization schemes used : 1, 2, 3

# Result comparison between different methods

**Scheme**|**dataset**|**dtype**|**input shape**|**detection period (sec)**|**FPS (CPU)**|**FPS (RPI)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
scheme1|coco|float32|300|20|0.1831|2.993
scheme2|coco|uint8|300|20|0.1565|**3.8588**
scheme3|coco|float32|640|20|6.4572|3.4039


