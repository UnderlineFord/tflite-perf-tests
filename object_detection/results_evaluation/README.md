## Results Evaluation

Evaluation of models/ experiements using the results json files saved [here](../results/coco2017_val) will be done. COCO2017 annotations which will be downloaded to [datasets directory](../datasets) which will be used as the ground truths for evaluations. 

### Evaluation steps:

```
cd object_detection/results_evaluation
pip -r install requirements.txt
bash save_results_outputs_csv.sh
```

Evaluation results will be saved in [here](results_output.csv).
