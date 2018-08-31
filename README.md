# Autonomous Driving Project - University of California, Irvine
> Autonomous Driving Project for the Center of Embedded and Cyber-physical Systems

![editedbanner](https://user-images.githubusercontent.com/20921475/42423185-27f6d328-82ab-11e8-9ce7-c45ada4244ec.png)

## Main Goal
Implement a CNN for Pedestian Detection on multiple cores inside embedded system (NVIDIA’s Drive PX2 platform)

## Object Detection History

### Viola-Jones Algorithm (2001)
Efficient Algorithm for face detection.
First time facial detection with webcam
= SVM trained on a dataset of faces

### HOG (Histogram of Oriented Gradients) (2005)
by Navneet Dalal & Bill Triggs
Algorithm for pedestrian detection
For every pixel, look at the pixels that directly surround it
Goal: How dark is current pixel compared to surrounding pixels?
1) draw an arrow showing in which direction the image is getting darker
2) Repeat that process for every pixel in the image
Each pixel is replaced by an arrow. These arrows are called gradients.
Following this, the image is divided into small squares of 16x16 pixels.
In each square, they would indicate the strongest direction.
=> Original image is represented by arrows that show a pattern (face, pedestrian, ...)
=> Compare it to other faces using similarity algorithms and then based on a specific treshold, classify as Face/notFace

### Convolutional Neural Networks (Deep Learning) (2012)
CNNs are now the gold standard for image classification
Why now?
1) lots of GPU & power
2) lots of Data

But when we, humans, look at the world around us, we don't just recognize objects, we are detecting different objects at the same time.
=> Build a bounded box
=> Identify relations

=> Take CNNs and repurpose them for these tasks.

Take the famous pre-trained classifiers by Google, etc ... like:
- VGG Net
- Inception V3
- ResNet
- GoogleNet 

We can then turn it into an object detector by sliding a small window across the image.
At each step, you run the CNN and identify and keep the ones the classifier is the most certain about.
This approach works but slow and not efficient.

=> A better approach was invented in 2015, **RCNNs**.

### Regions with Convolutional Neural Networks (Deep RCNNs) (2014)
RCNN creates bounding boxes, or regional proposals, using a process called **Selective Search**
At a higher level, Selective search looks at the image through windows of different sizes (randomly sized and placed windows at first), and then, for each size it tries to group together adjacent pixels by texture, color, or intensity to identify objects.
1) *Input* Image
2) Extract *Regions* Proposals using a specific treshold
3) Run the images in those boxes through a pretrained *CNN* like Inception or ResNet
4) *SVM* will classify and detect what image in the box is
5) Run the box through a *linear regression* model to output tighter coordinates for the box once the object has been classified.

**Improvements to RCNN**: 
- RCNN (paper 1)
- Fast RCNN (paper 2)
- Mask RCNN (paper 3)
- **YOLO**, outperformed all the other RCNNs

### YOLOv3 (You Only Look Once) (2014+)
by Ross Girshick (**Facebook AI Research**), Santosh Divvala (**Allen Institute for Artificial Intelligence**), Joseph Redmon (**University of Washington**), Ali Farhadi (**University of Washington**)

**(https://medium.com/@jonathan_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088)**


YOLO takes a different approach.
YOLO looks at the image once, hence its name, but in a clever way.
YOLO was trained on PASCAL VOC dataset which detects: cars, cats, dogd, persons, bycicles, boats, buses, traffic signs, ...

1) YOLO divides the image into a grid of 13x13 cells.
2) Each of these cells is responsible of predicting **5 bounding boxes**.
Bounding box = rectangle that encloses an object.
3) YOLO will output a confidence score that tells us how certain it is that the predicted box encloses an object.
(according to texture, color, patterns, intensity of pixels)
4) The higher this confidence score, the fatter the box is drawn. The confidence score doesn't say anything about  what kind of object is in the box, just if the shape of the box is good.
5) Each bounding box has a **1) confidence score of box existance** and **2) class (CNN)**.
6) The confidence score for the bounding box and the class prediction are combined into one final score that tells us the probability that this bounding box contains a specific type of object.
***Example***: 85% sure that the box contains *dog* => Based on a treshold that we decide, we can decide to leave or remove this bounding box.
7) Since 13x13x5=845 bounding boxes
=> most of these boxes have very low confidence scores, so we only keep the boxes whose final score is 30% or more (if threshold chosen is 0.3).

## Installation
Currently, YOLO is available in C but there's also a translation to Python using TensorFlow. 
You can choose to install the C version or the Python version on your computer.

#### C Version
https://pjreddie.com/darknet/yolo/

Download & Install
```sh
git clone https://github.com/pjreddie/darknet
cd darknet
make
```

Get the weights (You can choose to install smaller sized weights if you want like tiny-yolov3)
```sh
wget https://pjreddie.com/media/files/yolov3.weights
```

Run the algorithm
```sh
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
```

You can set the treshold if you want (0=show all the bounding boxes, 1=show only 100% accurate (which is almost never the case))
```sh
- treshold 0
```

Run the algorithm on a video
```sh
./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>
```

### Dependencies

### Training

## gem5
