# Fruit Detection in Orchards

#### Ripeness Analysis:
<img src = "/Detection Results/masked.png" width = "400">  <img src = "/Detection Results/scatterplot.png" width = "450"> 

<img src = "/Detection Results/analysis.png" width = "800">

Detection Results:

Yolov4 to the Left and Yolov5 to the Right

<img src = "/Detection Results/v4_aug_new/egif.gif" width = "300">  <img src = "/Detection Results/v5_new_aug/egif.gif" width = "300"> 

#### 29th July 2020

YoloV4 and V5 models are trained and tested under consistent conditions of augmentations and pre-processing.
### YoloV4 and YoloV5 Training Conditions:
Mangos are annotated in their respective formats which can be accessed from YoloV4 augmented Dataset and YoloV5 augmented Dataset folders.

#### Pre-Processing:
* Auto-orientation of pixel data  
* Resizing to 416x416

#### Augmentation:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Random rotation of between -15 and +15 degrees
* Random shear of between -15° to +15° horizontally and -15° to +15° vertically
* Random brigthness adjustment of between 0 and +85 percent
* Random exposure adjustment of between -27 and +27 percent
* Salt and pepper noise was applied to 1 percent of pixels

Here are the results obtained with their best weights.

| Parameters	| Yolov4(6000 epochs) 	| 	Yolov5(300 epochs)	| 	Yolov4-tiny(6000 epochs)		| Detectron 2		| Faster RCNN
|-------|--------|---------|--------|---------|---------|
| Precision	| 	0.76	| 	0.5676	| 	0.64	| 	 		| 
| Recall	  | 	0.83	| 	0.8427	| 	0.68	| 	 		| 
| F1-score	| 	0.80	| 	0.678	  | 	0.66	|  		  | 
| mAP@0.5 	|   0.82	|   0.791	  | 	0.6146	| 		|  		| 




### References and Similar Work Results.

|Title	 |    Architectures Used |	Data Augmentation Techniques |	Evaluation of Detection Performance |	Graphs Plotted | Results   
|-------|--------|---------|--------|---------| ---------|
| Deep Fruit Detection in Orchards | Faster R-CNN |Image Flipping and Rescaling | Tiling approach FR-CNN	| 	Average Precision Response Area under Precision Recall Curve, F1-score	Avg.Precision vs  Number of Training images|	F1 score > 0.9; Precision = 0.958; Recall = 0.863|
| Fast implementation of real-time fruit detection in apple orchards usingdeep learning | LedNet	|Two level scale amplification |	Average Precision Response, IoU, Precision, Recall|	Focal Loss and MSE functions vs Object confidence Score|	Recall = 0.821; Accuracy = 0.853|

