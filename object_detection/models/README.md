## Introdution

This directory contains the details of the models used for the comparison. 


## Methods used for model optimizations

* Influenced from this [official notebook](https://github.com/tensorflow/models/blob/master/research/object_detection/colab_tutorials/eager_few_shot_od_training_tflite.ipynb).

### 1. Method-1
```python
python object_detection/export_tflite_graph_tf2.py \
  --pipeline_config_path /content/$model_name/pipeline.config \
  --trained_checkpoint_dir /content/$model_name/checkpoint \
  --output_directory /content

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()
```

### 2. Method-2
```python
python object_detection/export_tflite_graph_tf2.py \
  --pipeline_config_path /content/$model_name/pipeline.config \
  --trained_checkpoint_dir /content/$model_name/checkpoint \
  --output_directory /content

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_data_gen
converter.inference_input_type = tf.uint8  
converter.inference_output_type = tf.uint8  
tflite_quant_model = converter.convert()
```

### 3. Method-3
```python
python object_detection/export_tflite_graph_tf2.py \
  --pipeline_config_path /content/$model_name/pipeline.config \
  --trained_checkpoint_dir /content/$model_name/checkpoint \
  --output_directory /content

tflite_convert --saved_model_dir=/content/saved_model --output_file=$output_dir
```


## Create tflite models

### 1. Method-1
* Download the complete **models** directory from [here](https://1drv.ms/u/s!AvriZdYzHLumoTuwMo0HXLCfHCMC?e=o71kcT) and replace with [the models directory](object_detection/models) manually.

### 2. Method-2

1. Create virtual environment
    ```python
    python -m venv ./get_tflite_env
    source get_tflite_env/bin/activate
    ```
  
1. create tflite models
    ```python
    cd tflite_perf_test/object_detection/models
    bash prepare_models.sh
    ```

### 3. Method-3
1. Create virtual environment
    ```python
    python -m venv ./get_tflite_env
    source get_tflite_env/bin/activate
    ```
  
1. Download and create selected tflite models
    ```python
    cd tflite_perf_test/object_detection/models
    bash requirements_for_tflite_conversion.sh
    bash tflite_conversion.sh ssd_mobilenet_v2 ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz
    ```



