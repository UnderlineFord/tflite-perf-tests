# Model details

* model name : ssd_mobilenet_v2_320x320_coco17_tpu-8
* downloaded from : [tf2 zoo](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection)

# Result comparison between different optimization schemes

**Optimization scheme**|**dataset**|**dtype**|**input shape**|**detection period (sec)**|**FPS (CPU)**|**FPS (RPI)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Dynamic|coco|float32|300|20|0.1831|2.993
Static|coco|uint8|300|20|0.1565|**3.8588**
Convert-only|coco|float32|640|20|6.4572|3.4039


