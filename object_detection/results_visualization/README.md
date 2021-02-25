## Results visualization

Visualizations of results using the results json files saved [here](../results/coco2017_val) will be done. Baseline results visualization is done using COCO2017 annotations which will be downloaded to [datasets directory](../datasets)

### Visualization steps:

```
cd object_detection/results_visualization
pip -r install requirements.txt
python visualize_results.py
```

Visualization results will be saved in this directory.

### Example visualization result

![Visualization results of "ssd_mobilenet_v1_1_default_model"](https://github.com/accelr-net/tflite-perf-tests/blob/main/object_detection/results_visualization/ssd_mobilenet_v1_1_default_model%40visualization.png)
