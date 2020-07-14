# Fruit Detection in Orchards -- (Latest Updates go first)


#### 13th July 2020 
|Title	 |    Architectures Used |	Data Augmentation Techniques |	Evaluation of Detection Performance |	Graphs Plotted | Results   
|-------|--------|---------|--------|---------| ---------|
| Deep Fruit Detection in Orchards | Faster R-CNN |Tiling approach FR-CNN |	Image Flipping and Rescaling| 	Average Precision Response Area under Precision Recall Curve, F1-score	Avg.Precision vs  Number of Training images|	F1 score > 0.9; Precision = 0.958; Recall = 0.863|
| Fast implementation of real-time fruit detection in apple orchards usingdeep learning | LedNet	|Two level scale amplification |	Average Precision Response, IoU, Precision, Recall|	Focal Loss and MSE functions vs Object confidence Score|	Recall = 0.821; Accuracy = 0.853|


####  Yolo-v5 Object detection model ---  Update : 12th July 2020  

Here are some insights I gathered after testing:

Both of them showed the same detection results with the test dataset although yolov5 was faster. But in very a few images yolov4 captured the occluded mangos very well.

When tested on data outside the test dataset, yolov4 has good detection results relatively.

Yolo v4 tiny detections to the left and that of Yolov5 to the right. 

<img src = "/Detection Results/Yolov4.gif" width = "300">  <img src = "/Detection Results/Yolov5.gif" width = "300"> 

<img src = "/Detection Results/Yolov5s-results.png" width = "800">  

####  Yolo-v4-tiny Object detection model ---  Update : 30th June 2020   

<img src = "/Detection Results/Yolov4-tiny results.png" width = "800"> 

#### Yolo-v4  Object detection model ---  Update : 28th June 2020   

 



