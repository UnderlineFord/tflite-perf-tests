# Introduction

This directory contains the details of the comparison of tflite models in object detection.

# Comparison results

* The results shown here is the **best results** obtained from each model using different optimization schemes shown in [here](models#methods-used-for-model-optimizations).

**Model**|**dataset**|**dtype**|**input shape**|**how quantized**|**FPS (RPI+CPP)**|**FPS (RPI+Python)**|**CPP- detected/ bbox correct**|**Python- detected/ bbox correct**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
[mobilenet\_object\_localizer ](models/mobile_object_localizer)|-|uint8|192|already quantized|32.3917|37.3974|YY|YN
[mobilenetv2\_danoorkans\_ayya](models/mobilenetv2_danoorkans_ayya)|-|uint8|300|already quantized|13.0855|13.0675|NN|NN
[ssd\_mobilenet\_v1](models/ssd_mobilenet_v1)|coco|uint8|300|already quantized|15.9551|13.752|YY|YY
[ssd\_mobilenet\_v1\_1 (default\_1)](models/ssd_mobilenet_v1_1%20(default_1))|-|uint8|300|already quantized|15.8794|15.2136|YY|YY
[ssd\_mobilenet\_v1\_fpn](models/ssd_mobilenet_v1_fpn)|coco|float32|640|[Convert only](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/models#3-convert-only-no-optimization)|-|0.0981|NN|YY
[ssd\_mobilenet\_v2](models/ssd_mobilenet_v2)|coco|uint8|300|[Static](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/models#2-static-integer-quantization-with-float-fallback-with-uint8-inference-input-type)|12.1224|12.3275|YY|YY
[ssd\_mobilenet\_v2\_fpnlite\_320x320](models/ssd_mobilenet_v2_fpnlite_320x320)|coco|float32|640|[Convert only](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/models#3-convert-only-no-optimization)|-|2.2380l|NN|YY
[ssd\_mobilenet\_v2\_fpnlite\_640x640](models/ssd_mobilenet_v2_fpnlite_640x640)|coco|float32|640|[Convert only](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/models#3-convert-only-no-optimization)|-|0.7179|NN|YY
[ssd\_mobilenet\_v3\_large](models/ssd_mobilenet_v3_large)|coco|uint8|320|already quantized|4.031|4.0618|YN|YY
[ssd\_mobilenet\_v3\_small](models/ssd_mobilenet_v3_small)|coco|uint8|320|already quantized|8.9612|8.9234|YN|YY


* FPS is calculated considering 20- 40 second interval from the starting time of model inferencing
* Num_threads of TensorFlow Lite Interpreter = 4

