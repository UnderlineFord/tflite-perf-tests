# Introduction

This directory contains the details of the comparison of tflite models in object detection.

# Comparison results

* The results shown here is the **best results** obtained from each model using different optimization schemes shown in [here](models#methods-used-for-model-optimizations).

**Model**|**dataset**|**dtype**|**input shape**|**how quantized**|**FPS (RPI+CPP)**|**FPS (RPI+Python)**|**detected/ bbox correct: CPP vs Python**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
[mobilenet\_object\_localizer ](models/mobile_object_localizer)|-|uint8|192|already quantized|32.3917|37.3974|YYYN
[mobilenetv2\_danoorkans\_ayya](models/mobilenetv2_danoorkans_ayya)|-|uint8|300|already quantized|13.0855|13.0675|NNNN
[ssd\_mobilenet\_v1](models/ssd_mobilenet_v1)|coco|uint8|300|already quantized|15.9551|13.752|YYYY
[ssd\_mobilenet\_v1\_1 (default\_1)](models/ssd_mobilenet_v1_1%20(default_1))|-|uint8|300|already quantized|15.8794|15.2136|YYYY
[ssd\_mobilenet\_v1\_fpn](models/ssd_mobilenet_v1_fpn)|coco|float32|640|[WithoutOpt](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/models/README.md#3-withoutopt-defeault-no-optimization-used)|-|fill|NNYY
[ssd\_mobilenet\_v2](models/ssd_mobilenet_v2)|coco|uint8|300|[IntQuantwFloatFallInpUint8](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/models/README.md#2-intquantwfloatfallinpuint8-integer-quantization-with-float-fallback-with-uint8-inference-input-type)|12.1224|12.3275|YYYY
[ssd\_mobilenet\_v2\_fpnlite\_320x320](models/ssd_mobilenet_v2_fpnlite_320x320)|coco|float32|640|[WithoutOpt](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/models/README.md#3-withoutopt-defeault-no-optimization-used)|-|fill|NNYY
[ssd\_mobilenet\_v2\_fpnlite\_640x640](models/ssd_mobilenet_v2_fpnlite_640x640)|coco|float32|640|[WithoutOpt](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/models/README.md#3-withoutopt-defeault-no-optimization-used)|-|fill|NNYY
[ssd\_mobilenet\_v3\_large](models/ssd_mobilenet_v3_large)|coco|uint8|320|already quantized|4.031|4.0618|YNYY
[ssd\_mobilenet\_v3\_small](models/ssd_mobilenet_v3_small)|coco|uint8|320|already quantized|8.9612|8.9234|YNYY


* FPS is calculated considering 20- 40 second interval from the starting time of model inferencing
* Num_threads of TensorFlow Lite Interpreter = 4

