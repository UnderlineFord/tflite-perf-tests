from visualization_utils import res2annot, draw_bboxes
import json
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os
import wget
import shutil
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

n_imgs=5

annotFile = f'../datasets/coco2017_val/instances_val2017.json' 
models=['ssd_mobilenet_v1_1_default_model', 'ssd_mobilenet_v2_method2', 'ssd_mobilenet_v3_large_model', 'ssd_mobilenet_v3_small_model']
n_bits=[32,64]
languages=['python', 'cpp']

if not os.path.isfile(annotFile):
  print('Downloading annotations ... ')
  try:os.mkdir('../datasets/coco2017_val/')
  except:pass
  wget.download('http://images.cocodataset.org/annotations/annotations_trainval2017.zip')
  shutil.unpack_archive('annotations_trainval2017.zip', '.')
  shutil.move('annotations/instances_val2017.json','../datasets/coco2017_val/')
  shutil.rmtree('annotations')
  os.remove('annotations_trainval2017.zip')


for model in models:
  res_python32=f"../results/coco2017_val/{model}@32bit@rpi@python@results.json"
  res_python64=f"../results/coco2017_val/{model}@64bit@rpi@python@results.json"
  res_cpp32=f"../results/coco2017_val/{model}@32bit@rpi@cpp@results.json"
  res_cpp64=f"../results/coco2017_val/{model}@64bit@rpi@cpp@results.json"

  resFiles=[res_python32, res_cpp32, res_python64, res_cpp64]

  _, annot_img_indices = res2annot(res_python32, annotFile, 'temp.json')  # to get annot image indices
  np.random.seed(144)
  img_ids= np.random.choice(annot_img_indices,n_imgs)

  plt.figure(figsize = (30, 5*n_imgs))

  for j in range(n_imgs):
    img_id = int(img_ids[j])

    plt.subplot(n_imgs,5,5*j+1)
    anns_annot = draw_bboxes(annotFile, img_id)
    plt.title('ground truth bboxes')
    for i in range(len(resFiles)):
      resFile= resFiles[i]
      output_file='res2annot.json'
      res_img_indices, annot_img_indices = res2annot(resFile, annotFile, output_file) 

      plt.subplot(n_imgs,5,5*j+i+2)
      anns_out = draw_bboxes(output_file, img_id)
      title= f"results_{resFile.split('@')[-2]}_{resFile.split('@')[-4]}"
      plt.title(title)
  plt.savefig(f'{model}@visualization')
  #plt.show()
os.remove('res2annot.json')
os.remove('temp.json')