#import sys
#sys.argv=['']

from cocoEval import get_stats

import os
import wget
import shutil
import argparse
import pandas as pd

## Download annotations
if not os.path.isfile('../datasets/coco2017_val/instances_val2017.json'):
  print('Downloading annotations ... ')
  try:os.mkdir('../datasets/coco2017_val/')
  except:pass
  wget.download('http://images.cocodataset.org/annotations/annotations_trainval2017.zip')
  shutil.unpack_archive('annotations_trainval2017.zip', '.')
  shutil.move('annotations/instances_val2017.json','../datasets/coco2017_val/')
  shutil.rmtree('annotations')
  os.remove('annotations_trainval2017.zip')

## Evaluating models given the conditions

def evaluate_models(models, n_bit=32, language='python', coco_dataset_version='2017', num_threads=4):
  stats= {}
  for model in models:
    if num_threads==1:result_file = f'{model}@{n_bit}bit@rpi@{language}@results_numthreads1.json'
    else:result_file = f'{model}@{n_bit}bit@rpi@{language}@results.json'

    if 'sample' in result_file:continue
    if '.json' not in result_file:continue

    #print(result_file)
    result_dir = f'../results/coco{coco_dataset_version}_val/{result_file}'
    annot_dir = f'../datasets/coco{coco_dataset_version}_val/instances_val{coco_dataset_version}.json' 
    stats[result_dir] = get_stats(annFile= annot_dir, resFile= result_dir)
  return stats

def save_stats(out_csv, stats_dict=None, overwrite=False):
  results_dict = {}
  for key in stats_dict:
    if 'numthreads1' in key:continue
    coco_version = key.split('/')[2][4:8]
    file_name = key.split('/')[3]

    model, n_bit, hardware, language, type_ = file_name[:-5].split('@')

    if type_!='results' or hardware!='rpi':continue

    if model not in results_dict:results_dict[model]={}
    print(f'{n_bit}RPI_{language}')
    results_dict[model][f'{n_bit}RPI_{language}']=stats_dict[key][0]
    results_df = pd.DataFrame(results_dict).T

    #for column_name in ["32bitRPI_python","32bitRPI_cpp","64bitRPI_python","64bitRPI_cpp"]:
    #  if f'{n_bit}RPI_{language}'== column_name:continue
    #  results_df[column_name] ='NA'


  if overwrite:
    results_df.to_csv(out_csv, mode='w', header=True)
  else:
    results_df.to_csv('temp.csv', mode='w', header=True)
    
    csv_df = pd.read_csv(out_csv)
    results_df = pd.read_csv('temp.csv')
    print(csv_df, results_df)
    results_df = pd.merge(csv_df, results_df, on="Unnamed: 0")
    results_df.to_csv(out_csv, mode='w', header=True, index=False)

    os.remove('temp.csv')

  return results_df


if __name__ == "__main__":
  models = ['ssd_mobilenet_v3_small_model', 'ssd_mobilenet_v3_large_model', 'ssd_mobilenet_v2_method2', 'ssd_mobilenet_v1_1_default_model']

  parser = argparse.ArgumentParser(description='Object Detection')
  parser.add_argument('--n_bit', type=str, help='Specify the bits in RPI OS', default=32)
  parser.add_argument('--language', type=str, help='Specify the language', default='python')
  parser.add_argument('--coco_dataset_version', type=str, help='Specify the coco dataset version', default='2017')
  parser.add_argument('--num_threads', type=str, help='Specify the num_threads used to train', default=4)
  parser.add_argument('--output_csv_file', type=str, help='Specify the output file to save results', default=None)
  parser.add_argument('--overwrite', type=str, help='Specify whether the overwrite/ append data to the file', default='False')


  args = parser.parse_args()

  n_bit=args.n_bit
  language=args.language 
  output_csv_file=args.output_csv_file
  overwrite= (args.overwrite =='True')

  coco_dataset_version=args.coco_dataset_version
  num_threads=args.num_threads

  stats = evaluate_models(models, n_bit=n_bit, language=language, coco_dataset_version=coco_dataset_version, num_threads=num_threads)

  if output_csv_file!=None:
    print(f'Writing to file ... {output_csv_file} :: OVERWRITE : {overwrite}')
    added_df = save_stats(out_csv= output_csv_file, stats_dict=stats, overwrite=overwrite)
    print('writing successful')
  else:print('Writing to file is not done')