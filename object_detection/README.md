# Introduction

This directory contains the details of the comparison of tflite models in object detection.

# Comparison results

* The results shown here is the **best results** obtained from each model using different optimization methods shown in [here](models#methods-used-for-model-optimizations).

**Model**|**dataset**|**dtype**|**input shape**|**how quantized**|**detection period (sec)**|**FPS (CPU)**|**FPS (RPI)**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
[mobilenet\_object\_localizer ](models/mobile_object_localizer)|-|uint8|192|already quantized|10|6.7097|12.7345
[mobilenetv2\_danoorkans\_ayya](models/mobilenetv2_danoorkans_ayya)|-|uint8|300|already quantized|10|2.1886|4.3399
[ssd\_mobilenet\_v1](models/ssd_mobilenet_v1)|coco|uint8|300|already quantized|10|2.3259|5.4281
[ssd\_mobilenet\_v1\_1 (default\_1)](models/ssd_mobilenet_v1_1%20(default_1))|-|uint8|300|already quantized|10|2.2539|5.3809
[ssd\_mobilenet\_v1\_fpn](models/ssd_mobilenet_v1_fpn)|coco|float32|640|[Scheme3](models/README.md#3-scheme-3-default)|20|0.2863|0.1218
[ssd\_mobilenet\_v2](models/ssd_mobilenet_v2)|coco|uint8|300|[Scheme2](models/README.md#2-scheme-2-integer-quantization-with-float-fallback-with-uint8-inference-input-type)|20|0.1565|3.8588
[ssd\_mobilenet\_v2\_fpnlite\_320x320](models/ssd_mobilenet_v2_fpnlite_320x320)|coco|float32|640|[Scheme3](models/README.md#3-scheme-3-default)|20|4.5612|2.4678
[ssd\_mobilenet\_v2\_fpnlite\_640x640](models/ssd_mobilenet_v2_fpnlite_640x640)|coco|float32|640|[Scheme3](models/README.md#3-scheme-3-default)|20|1.1954|0.7038
[ssd\_mobilenet\_v3\_large](models/ssd_mobilenet_v3_large)|coco|uint8|320|already quantized|10|7.1549|3.9996
[ssd\_mobilenet\_v3\_small](models/ssd_mobilenet_v3_small)|coco|uint8|320|already quantized|10|18.8569|9.7913



