
import json
import os
import shutil
import wget


def read_text(n_bits_rpi=64):
  n_bits= n_bits_rpi
  data_dict = {}
  for model in os.listdir(f'cpp{n_bits}bit_file_structure/save_outputs'):
    if os.path.isfile(f"cpp{n_bits}bit_file_structure/save_outputs/{model}/results.txt"):
      results_dir = f"cpp{n_bits}bit_file_structure/save_outputs/{model}/results.txt"
      with open(results_dir, 'r') as f:
        data = f.read()
        print('reading from : ',results_dir)
      if ' (default_1)' in model:model=model[:-12]+'_default'
      data_dict[model+'_model']= data
    else:
      for method in os.listdir(f"cpp{n_bits}bit_file_structure/save_outputs/{model}"):
        results_dir = f"cpp{n_bits}bit_file_structure/save_outputs/{model}/{method}/results.txt"
        if not os.path.isfile(results_dir):continue
        
        with open(results_dir, 'r') as f:
          data = f.read()
          print('reading from : ',results_dir)
        if ' (default_1)' in model:model=model[:-12]
        data_dict[model+f'_{method}']= data
  print('\n\n')
  return data_dict
def get_correct_results_format(data_dict):
  for key in data_dict.keys():
    bboxes = data_dict[key].strip().split('\n')

    for i in range(len(bboxes)):
      bbox_details = bboxes[i].strip().split(' ')

      img_id = int(bbox_details[0])
      class_ = int(bbox_details[1])+1
      score = float(bbox_details[2])
      ymin,xmin,ymax,xmax = float(bbox_details[3]), float(bbox_details[4]), float(bbox_details[5]),float(bbox_details[6])
      (left, right, top, bottom) = (xmin, xmax, ymin, ymax)
      width=right-left
      height=bottom-top

      bbox_details_dict = {'image_id':img_id, 'category_id': class_, 'score': score, 'bbox':[xmin, ymin, width, height]}
      bboxes[i]=bbox_details_dict

    data_dict[key] = bboxes
  return data_dict
def save_correct_results(correct_results_dict, n_bit=64, hardware='rpi'):
  out_files=[]
  for key in correct_results_dict.keys():
    results = correct_results_dict[key]
    out_file = f'results/coco2017_val/{key}@{n_bit}bit@{hardware}@cpp@results.json'
    with open(out_file, 'w') as f:
      json.dump(results, f)
    out_files.append(out_file)
  return out_files


if __name__ == "__main__":
  os.chdir('../')

  if not os.path.isfile('datasets/coco2017_val/instances_val2017.json'):
    print('Downloading annotations ... ')
    try:os.mkdir('datasets/coco2017_val/')
    except:pass
    wget.download('http://images.cocodataset.org/annotations/annotations_trainval2017.zip')
    shutil.unpack_archive('annotations_trainval2017.zip', '.')
    shutil.move('annotations/instances_val2017.json','datasets/coco2017_val/')
    shutil.rmtree('annotations')
    os.remove('annotations_trainval2017.zip')


  n_bits_rpi=32
  data_dict = read_text(n_bits_rpi=n_bits_rpi)
  correct_data_dict = get_correct_results_format(data_dict)
  out_files = save_correct_results(correct_data_dict, n_bit= n_bits_rpi)

  print(out_files)
