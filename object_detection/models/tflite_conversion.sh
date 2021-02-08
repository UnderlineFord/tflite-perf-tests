#!/bin/bash

cd ../../../models/research
base_dir='../../tflite_perf_test/object_detection/models'

### INPUTS
model_dir_name_init="$1"
model="$2"

model_dir_name="${base_dir}/${model_dir_name_init}"
model_name=$(echo "$model" | cut -d'.' -f 1)
raw_model_dir="$model_dir_name/raw_model"
raw_model="${model_dir_name}/raw_model/${model_name}"
saved_model="$model_dir_name/saved_model"

tflite_model="$model_dir_name/method5.tflite"


mkdir -p "$raw_model_dir"
wget "http://download.tensorflow.org/models/object_detection/tf2/20200711/$model"
tar -C "$raw_model_dir" -zxvf "$model"
rm "$model"

python object_detection/export_tflite_graph_tf2.py \
    --pipeline_config_path $raw_model/pipeline.config \
    --trained_checkpoint_dir $raw_model/checkpoint \
    --output_directory $model_dir_name

tflite_convert --saved_model_dir=$saved_model --output_file=$tflite_model

cd ../../tflite_perf_test/object_detection/models/

python tflite_convert2.py --model_dir_name $model_dir_name_init --model $model 