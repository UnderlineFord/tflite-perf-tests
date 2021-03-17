
# Introduction

* This repository contained the latency benchmarks (FPS rates) obtained from different tflite models with different optimization patterns. 
* Tests have been conducted on RPI and WSL (on CPU). Specifications are mentioned in [below](#specifications).
* Python and C++ are used for the implementations.


# Specifications

* python version               : 3.7.3
* RPI version                  : 
	1. 32 bit : Raspbian GNU/Linux 10 \n \l ::: Linux raspberrypi 5.4.72-v7l+ #1356 SMP Thu Oct 22 13:57:51 BST 2020
	2. 64 bit : Debian GNU/Linux 10 \n \l ::: Linux raspberrypi 5.4.79-v8+ #1373 SMP PREEMPT Mon Nov 23 13:32:41 GMT 2020 aarch64 GNU/Linux
* WSL version                  : Linux acerf15 4.4.0-19041-Microsoft #488-Microsoft Mon Sep 01 13:43:00 PST 2020 x86_64 x86_64 x86_64 GNU/Linux

# Installation steps for RPI/ WSL (Python)

## 1. 32bit RPI

### 1. Image classification
1. Create virtual environment

	```python
	python3 -m venv tflite_perf_test_env
	source tflite_perf_test_env/bin/activate
	```

1. Clone the repository

	```python
	git clone https://github.com/accelr-net/tflite-perf-tests.git
	```

1. Install requirements
	* The correct version of [tflite_runtime](https://www.tensorflow.org/lite/guide/python) can be found using [this guide](https://www.tensorflow.org/lite/guide/python#install_just_the_tensorflow_lite_interpreter).
	
	1. for WSL
		```python
		cd tflite_perf_test
		pip3 install https://github.com/google coral/pycoral/releases/download/release frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_x86_64.whl
		pip3 install -r requirements.txt
		```

	1. for RPI
		```python
		cd tflite_perf_test
		pip3 install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl
		pip3 install -r requirements.txt
		```


1. Download tflite models
	```python
	cd ..
	wget https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224_quant.tgz
	tar -xvzf mobilenet_v1_1.0_224_quant.tgz
	mv ./mobilenet_v1_1.0_224_quant.tflite ./tflite_perf_test/image_classification/models/mobilenet_v1/model.tflite
	```

1. Run image_classification.py
	```python
	cd image_classification
	python image_classification.py
	```

### 2. Object detection 
1. Create virtual environment
	```python
	python3 -m venv tflite_perf_test_env
	source tflite_perf_test_env/bin/activate
	```
1. Clone the repository
	```python
	git clone https://github.com/accelr-net/tflite-perf-tests.git
	```

2. Install requirements
	* The correct version of [tflite_runtime](https://www.tensorflow.org/lite/guide/python) can be found using [this guide](https://www.tensorflow.org/lite/guide/python#install_just_the_tensorflow_lite_interpreter).

	1. for WSL: 
		```python
		cd tflite_perf_test
		pip3 install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_x86_64.whl
		pip3 install -r requirements.txt
		```

	2. for RPI
		```python
		cd tflite_perf_test
		pip3 install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl
		pip3 install -r requirements.txt
		```

3. Create tflite models
	1. Method 1: Download the complete **models** directory from [here](https://1drv.ms/u/s!AvriZdYzHLumoTuwMo0HXLCfHCMC?e=o71kcT) and replace with [the models directory](object_detection/models) manually.
	2. Method 2: Use [prepare_models.sh](object_detection/models/prepare_models.sh) as mentioned [here](https://github.com/udithh-accelr/test-repo/tree/main/object_detection/models#2-method-2-1) to create tflite models
	3. Method 3: Manually download and convert models using the guidelines [here](https://github.com/udithh-accelr/test-repo/tree/main/object_detection/models#3-method-3-1)

4. Run object_detection.py for evaluate only FPS on [sample dataset](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/sample_images)
	```python
	cd object_detection 
	python object_detection.py --model_path models/ssd_mobilenet_v3_small/model.tflite --label_path models/default_setting/coco_labelmap.txt
	```
5. Run object_detection_with_cocoeval.py for evaluating FPS and calculating mAP for COCO dataset simultaneously (Use proper arguments/ Tested only on RPI)
	```python
	cd object_detection 
	python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v3_small/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False
	```
	
	* This creates results/ prediction files (json) which will be saved in [here](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/results/coco2017_val). Those can be used for [visualization the bounding boxes](https://github.com/accelr-net/tflite-perf-tests#visualization)/ [Accuracy evaluation](https://github.com/accelr-net/tflite-perf-tests#accuracy-evaluation).


## 2. 64bit RPI

### Object detection 

* 64bit OpenCV, Numpy are built according to [this article](https://qengineering.eu/install-opencv-4.5-on-raspberry-64-os.html).
* The correct version of [tflite_runtime](https://www.tensorflow.org/lite/guide/python) can be found using [this guide](https://www.tensorflow.org/lite/guide/python#install_just_the_tensorflow_lite_interpreter).
	```python
	pip3 install tflite runtime : https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_aarch64.whl
	```
* Other instructions are same as in the [32-bit object detection installation steps](https://github.com/accelr-net/tflite-perf-tests/blob/main/README.md#2-object-detection).
* Step-5 in [32-bit object detection installation steps](https://github.com/accelr-net/tflite-perf-tests/blob/main/README.md#2-object-detection) should be changed as follows,
	```python
	cd object_detection 
	python3 object_detection_with_cocoeval.py --model_path models/ssd_mobilenet_v3_small/model.tflite --save_results True --image_path 'datasets/coco2017_val/images' --coco_dataset_version='2017' --is_baseline=False --n_bit=64
	```

# Installation steps for RPI (C++)

## 1. 32 bit RPI

### Object detection 

* Tensorflow Lite installation and environment setup has been done according to [this article](https://qengineering.eu/install-tensorflow-2-lite-on-raspberry-pi-4.html) and [this repository](https://github.com/Qengineering/TensorFlow_Lite_SSD_RPi_32-bits)
* TFLite models obtained as explained in *Create tflite models section* [here](https://github.com/accelr-net/tflite-perf-tests#2-object-detection)
* Performance evaluations were done using [this script](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/object_detection_get_fps_only.cpp) based on the [sample dataset](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/sample_images)
* Performance evaluation and results saving both can be done simultaneously using [this script](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/object_detection_save_results.cpp).
	* This saves the results/ predictions as txt files inside the corresponding directory.
	* Those txt files should be converted to json format using the steps explained [here](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/cpp32bit_file_structure).
	* This created results/ prediction files (json) will be saved in [here](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/results/coco2017_val). 
	* Those can be used for [visualization the bounding boxes](https://github.com/accelr-net/tflite-perf-tests#visualization)/ [Accuracy evaluation](https://github.com/accelr-net/tflite-perf-tests#accuracy-evaluation).

## 2. 64 bit RPI

### Object detection 

* Tensorflow Lite installation and environment setup has been done according to [this article](https://qengineering.eu/install-tensorflow-2-lite-on-raspberry-64-os.html) and [this repository](https://github.com/Qengineering/TensorFlow_Lite_SSD_RPi_64-bits)
* TFLite models obtained as explained in *Create tflite models section* [here](https://github.com/accelr-net/tflite-perf-tests###2-object-detection)
* Performance evaluations were done using [this script](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/object_detection_get_fps_only.cpp) based on the [sample dataset](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/sample_images)
* Performance evaluation and results saving both can be done simultaneously using using [this script](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/object_detection_save_results.cpp).
	* This saves the results/ predictions as txt files inside the corresponding directory.
	* Those txt files should be converted to json format using the steps explained [here](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/cpp64bit_file_structure).
	* This created results/ prediction files (json) will be saved in [here](https://github.com/accelr-net/tflite-perf-tests/tree/main/object_detection/results/coco2017_val). 
	* Those can be used for [visualization the bounding boxes](https://github.com/accelr-net/tflite-perf-tests#visualization)/ [Accuracy evaluation](https://github.com/accelr-net/tflite-perf-tests#accuracy-evaluation).

# Results- Object Detection

## FPS speed evaluation
* Final results comparison is found in [here](object_detection/README.md#comparison-results)

## Accuracy evaluation
* Accuracy evaluations and instructions can be found [here](object_detection/results_evaluation)

## Visualization
* Visualization of results and instructions can be found [here](object_detection/results_visualization)




