# Introduction

This directory contains the details of the comparison of tflite models in object detection.

# Comparison results

### Results on popular models

| Experiment| 1. ssd_mobilenet_v3_small | 2. ssd_mobilenet_v3_large | 3. ssd_mobilenet_v2 (II- STATIC)  | 4. ssd_mobilenet_v1_1 |
|:-----:|:-----:|:-----:|:-----:|:-----:|
| baseline |8.2447|2.9859| 4.0262 | 5.4377|
| 32bit C++|NA|NA| 12.649 | 16.2938|
| 32bit Python|8.7626|3.918| 12.8385| 16.6009|
| 64bit C++|NA|NA| 17.153 | 22.8117|
| 64bit Python|18.475|8.1404| 17.0597| 22.2758|

* Raspberry Pi 4B [Aluminium Heatsink Case with Dual Fans](https://makerstation.lk/product/heat-sink-aluminum-casing-with-fan/) are used to minimize excessive heating of the device during inference runs.
* FPS calculated using COCO2017 validation set as explained in [step 6 here](https://github.com/accelr-net/tflite-perf-tests#2-object-detection).
* Complete results comparison with details can be found [here]([results_comparison](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/TFLITE_PERF_TEST-COMPARISON.xlsx))

### Results of other methods/ models

| Model| 32 bit C++ : FPS | 32bit C++ : detected/ bbox correct | 32 bit Python : FPS | 32bit Python :detected/ bbox correct | 64 bit C++ : FPS | 64bit C++ :detected/ bbox correct | 64 bit Python : FPS | 64bit Python : detected/ bbox correct |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|

| 1\. ssd\_mobilenet\_v3\_small | 8.9612 | YN | 8.9234 | YY | 16.4866 | YN | 19.9146 | YY |
| 2\. ssd\_mobilenet\_v3\_large | 4.031   | YN | 4.0618 | YY | 7.4348  | YN| 8.7249 | YY |
| 3\. ssd\_mobilenet\_v2\_fpnlite\_640 (I- DYNAMIC) | \- | \- | 0.6604 | YY | \- | \- | 1.1753 | YY |
| 3\. ssd\_mobilenet\_v2\_fpnlite\_640 (III- CONVERT-ONLY) | \- | | 0.7179 | YY | \- || 1.3288 | YY |
| 4\. ssd\_mobilenet\_v2\_fpnlite\_320 (I- DYNAMIC) | \- | \- | 1.9446 | YY | \- | \- | 4.3872 | YY |
| 4\. ssd\_mobilenet\_v2\_fpnlite\_320 (III- CONVERT-ONLY) | \- | \- | 2.238  | YY | \- | \-| 5.1319 | YY    |
| 5\. ssd\_mobilenet\_v2 (II- STATIC) | 12.1224 | YY | 12.3275| YY | 15.1486 | YY| 14.2964| YY |
| 6\. ssd\_mobilenet\_v1\_fpn (I- DYNAMIC) | \- | \- | 0.2527 | YY | \- | \-| 0.2725 | YY |
| 6\. ssd\_mobilenet\_v1\_fpn (III- CONVERT-ONLY) | \- | \- | 0.0981 | YY   | \- | \-| 0.1087 | YY |
| 7\. ssd\_mobilenet\_v1\_1 | 15.8794 | YY | 15.2136| YY   | 19.4072 | YY| 19.2025| YY |
| 8\. ssd\_mobilenet\_v1  | 15.9551 | YY | 13.752 | YY | 19.6126 | YY| 19.0989| YY |
| 9\. Mobilenet v2- face detector | 13.0855 | NN | 13.0675| NN | 16.9024 | NN| 14.2139| NN |
| 10\. example (they given for CPP) | 15.1958 | YY | \- | \-   | 19.3783 | YY| \- | \- |
| 11\. localizer | 32.3917 | YN | 37.3974| YY   | 38.4623 | YN| 35.7587| YY |


* FPS results and results types of all models are shown
* calculated using sample_datasets as explained in [step 5 here](https://github.com/accelr-net/tflite-perf-tests#2-object-detection).
* calculated considering 20- 40 second interval from the starting time of model inferencing
* Num_threads of TensorFlow Lite Interpreter = 4
* Results obtained with no fans/ heat sinks
* FPS calculation was done using initial methods on both C++, Python
* obtained mAP values for important experiments can be found in "all_results"/ "results_important" in [results_comparison](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/TFLITE_PERF_TEST-COMPARISON.xlsx)
