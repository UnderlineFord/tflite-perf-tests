
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import tensorflow as tf
import pathlib
import argparse

img_dir='../sample_images/*'
base_dir='.'

### INPUTS
parser = argparse.ArgumentParser(description='Object Detection')
parser.add_argument('--model_dir_name', type=str, help='Specify the directory name', default='ssd_mobilenet_v2')
parser.add_argument('--model', type=str, help='Specify the model file', default='ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz')
args = parser.parse_args()

model_dir_name=args.model_dir_name
model=args.model

###
model_dir_name=f'{base_dir}/{model_dir_name}'
model_name=model[:-7]
raw_model_dir=f"{model_dir_name}/raw_model"
raw_model=f'{model_dir_name}/raw_model/{model_name}'
saved_model=f"{model_dir_name}/saved_model"

def representative_data_gen():
  inp_shape=300
  dataset_list = tf.data.Dataset.list_files(img_dir)
  for i in range(100):
    image = next(iter(dataset_list))
    image = tf.io.read_file(image)
    image = tf.io.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [inp_shape, inp_shape])
    image = tf.cast(image / 255., tf.float32)
    image = tf.expand_dims(image, 0)
    yield [image]

def save_model(tflite_quant_model,method_number='2'):
  model_dir=f'{model_dir_name}/method{method_number}.tflite'
  tflite_model_file=pathlib.Path(model_dir)
  tflite_model_file.write_bytes(tflite_quant_model)

def method1():
  converter = tf.lite.TFLiteConverter.from_saved_model(saved_model)
  converter.optimizations = [tf.lite.Optimize.DEFAULT]
  tflite_quant_model = converter.convert()
  save_model(tflite_quant_model, '1')

def method2():
  inp_shape=300
  try:
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    converter.representative_dataset = representative_data_gen
    converter.inference_input_type = tf.uint8  # or tf.uint8
    converter.inference_output_type = tf.uint8  # or tf.uint8
    tflite_quant_model = converter.convert()
    save_model(tflite_quant_model,'2')
  except:print('error: check inputs')

def method3():
  try: 
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.representative_dataset = representative_data_gen
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8,tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
    converter.inference_input_type = tf.uint8  # or tf.uint8
    converter.inference_output_type = tf.uint8  # or tf.uint8
    tflite_quant_model = converter.convert()
    save_model(tflite_quant_model,'3')
  except:print('error: check inputs')


method1()
method2()
method3()