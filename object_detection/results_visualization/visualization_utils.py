import json
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

def res2annot(resFile, annotFile, output_file='res2annot.json'):
  with open(resFile) as f:
    res_data= json.load(f)
  with open(annotFile) as f:
    annot_data= json.load(f)
  
  new_res_data=[]
  for i in range(len(res_data)):
    res=res_data[i]
    res['id']=i
    res['segmentation']=[]
    new_res_data.append(res)

  
  res_img_indices, annot_img_indices=[],[] # to store image_ids in results.json and annot.json 
  for i in range(len(res_data)):
    res_img_indices.append(res_data[i]['image_id'])
  for i in range(len(annot_data['annotations'])):
    annot_img_indices.append(annot_data['annotations'][i]['image_id'])

  annot_data['annotations'] = new_res_data

  with open(output_file, 'w') as f:
    json.dump(annot_data,f)

  return list(set(res_img_indices)), list(set(annot_img_indices))

def draw_bboxes(annFile, img_ids=[324158]):
  coco=COCO(annFile)

  # get all images containing given categories, select one at random
  #catIds = coco.getCatIds(catNms=['person','dog','skateboard']);
  catIds = coco.getCatIds();
  imgIds = coco.getImgIds(catIds=catIds);
  imgIds = coco.getImgIds(imgIds = img_ids) #indices are obtained from coco.imgs : add 146457,129492, etc if wanted
  img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

  # load and display instance annotations
  I = io.imread(img['coco_url'])
  plt.imshow(I); plt.axis('off')
  annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
  anns = coco.loadAnns(annIds)
  coco.showAnns(anns, True)
  return anns