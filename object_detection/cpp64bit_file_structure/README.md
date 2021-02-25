# C++ 64bit Experiments 

## Directories

* save_outputs : consists of models directories with corresponding C++ evaluation script and results.txt containing the results saved by that script.
* fps_evaluation : consists of models directories with corresponding C++ evaluation scripts which does fps evaluation on sample_images (results are not saved). 
    * C++ scripts for this fps calculation can be found [here](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/object_detection.cpp)

## Converting results.txt files to results-evaluation-friendly json formats:
```
cd cpp64bit_file_structure
pip install -r requirements.txt
python convert_cpp64_txt2json.py
```

* Corresponding results results-evaluation-friendly json files will be saved in [../results/coco2017_val](../results/coco2017_val)
* This json files will be used for [results_evaluation](../results_evaluation) and [results_visualization](../results_visualization)
