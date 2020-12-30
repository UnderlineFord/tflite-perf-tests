
# Introduction

* This repository contained the latency benchmarks (FPS rates) obtained from different tflite models with different optimization patterns. 
* Tests have been conducted on RPI and WSL (on CPU). Specifications are mentioned in [below](#specifications).
* Python and C++ are used for the implementations.


# Specifications

* python version               : 3.7.3
* RPI version                  : RPI OS (32-bit)- Linux (ARM 32) -recommended:: Raspbian GNU/Linux 10 \n \l ::: Linux raspberrypi 5.4.72-v7l+ #1356 SMP Thu Oct 22 13:57:51 BST 2020
* WSL version                  : Linux acerf15 4.4.0-19041-Microsoft #488-Microsoft Mon Sep 01 13:43:00 PST 2020 x86_64 x86_64 x86_64 GNU/Linux

# Installation steps for RPI/ WSL (Python)


## 1. Image classification
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

## 2. Object detection 
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

4. Run object_detection.py
	```python
	cd object_detection 
	python object_detection.py --model_path models/ssd_mobilenet_v2_fpnlite_320x320/method5.tflite --label_path models/default_setting/coco_labelmap.txt
	```
# Installation steps for RPI (C++)

## Object detection 

* Tensorflow Lite installation and environment setup has been done according to [this article](https://qengineering.eu/install-tensorflow-2-lite-on-raspberry-pi-4.html) and [this repository](https://github.com/Qengineering/TensorFlow_Lite_SSD_RPi_32-bits)
* TFLite models obtained as explained in *Create tflite models section* [here](https://github.com/accelr-net/tflite-perf-tests#2-object-detection)
* Performance evaluations were done using [this script](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/object_detection.cpp)



# Results
* Final results comparison is found in [here](object_detection/README.md#comparison-results)
