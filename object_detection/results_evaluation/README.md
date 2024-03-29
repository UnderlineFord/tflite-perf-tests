# Results Evaluation

Evaluation of models/ experiements using the results json files saved [here](../results/coco2017_val) will be done. COCO2017 annotations which will be downloaded to [datasets directory](../datasets) which will be used as the ground truths for evaluations. 

## Evaluation steps:

```
cd object_detection/results_evaluation
pip install -r requirements.txt
bash save_results_outputs_csv.sh
```

Evaluation results will be saved in [here](results_output.csv).

## Details of Evaluation Metrics

[COCO evaluation metrics](https://cocodataset.org/#detection-eval) were used. Only COCO **AP at IoU=.50:.05:.95 (primary challenge metric)** will be saved in the [results csv file](results_output.csv).


### COCO Evaluation Metrics

![coco evaluation metrics](evaluation_metrics.png)


