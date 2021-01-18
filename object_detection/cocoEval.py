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

parser = argparse.ArgumentParser(description='Object Detection')
parser.add_argument('--dataType', type=str, help='Specify the model path', default='val2014')
parser.add_argument('--dataDir', type=str, help='Specify the label map', default='.')
parser.add_argument('--resultsFile', type=str, help='Specify the results file (.json format)', default=None)
parser.add_argument('--annotationFile', type=str, help='Specify the annotation file (.json format)', default='datasets/coco2014_val/instances_val2014.json')

args = parser.parse_args()

dataType=args.dataType
dataDir=args.dataDir
annFile=args.annotationFile
resFile=args.resultsFile

#initialize COCO ground truth api
annType = 'bbox'     #specify type here
if annFile==None:
    prefix = 'instances'
    print('Running demo for *%s* results.'%(annType))
    annFile = '%s/annotations/%s_%s.json'%(dataDir,prefix,dataType) # annotation file
else:
    print(f'\nloading annotation file from : {annFile}')
cocoGt=COCO(annFile)

#initialize COCO detections api
if resFile==None:
    resFile='%s/results/%s_%s_fake%s100_results.json'  
    resFile = resFile%(dataDir, prefix, dataType, annType)   # results file
else:
    print(f'\nloading results file from : {resFile}')
cocoDt=cocoGt.loadRes(resFile)

imgIds=sorted(cocoGt.getImgIds())
imgIds=imgIds[0:100]
imgId = imgIds[np.random.randint(100)]

# running evaluation
cocoEval = COCOeval(cocoGt,cocoDt,annType)
cocoEval.params.imgIds  = imgIds
cocoEval.evaluate()
cocoEval.accumulate()

cocoEval.summarize()
