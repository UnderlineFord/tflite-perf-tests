# Model details

* model name : ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8
* downloaded from : [tf2 zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) 

# Result comparison between different optimization schemes

**Optimization scheme**|**dataset**|**dtype**|**input shape**|**detection period (sec)**|**FPS (CPU)**|**FPS (RPI)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Dynamic|coco|float32|640|20|0.0021|0.0972
Convert-only|coco|float32|640|20|0.2863|**0.1218**


