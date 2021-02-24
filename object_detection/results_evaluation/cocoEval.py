
'''
Inputs:
* resultsFile (json) and annotationFile(json) can be directly fed
* If not -> those files should be in the directories such as "./annotations/instances_val2014.json" and "./results/instances_val2014_fakebbox100_results.json"
'''

import matplotlib.pyplot as plt
import argparse
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import skimage.io as io
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)

def get_stats(annFile, resFile):
  print(f'\nloading annotation file from : {annFile}')
  cocoGt=COCO(annFile)

  print(f'\nloading results file from : {resFile}')
  cocoDt=cocoGt.loadRes(resFile)

  imgIds=sorted(cocoGt.getImgIds())
  imgIds=imgIds[0:100]
  imgId = imgIds[np.random.randint(100)]

  # running evaluation
  cocoEval = COCOeval(cocoGt,cocoDt,'bbox')
  cocoEval.params.imgIds  = imgIds
  cocoEval.evaluate()
  cocoEval.accumulate()

  cocoEval.summarize()
  stats= cocoEval.stats
  return stats

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Object Detection')
  parser.add_argument('--resultsFile', type=str, help='Specify the results file (.json format)', default=None)
  parser.add_argument('--annotationFile', type=str, help='Specify the annotation file (.json format)', default='datasets/coco2017_val/instances_val2017.json')

  args = parser.parse_args()

  stats = get_stats(args.annotationFile, args.resultsFile)