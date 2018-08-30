# Autonomous Driving Project - UC Irvine
Autonomous Driving Project for the Center of Embedded and Cyber-physical Systems

![editedbanner](https://user-images.githubusercontent.com/20921475/42423185-27f6d328-82ab-11e8-9ce7-c45ada4244ec.png)

## Main Goal
Implement a CNN for Pedestian Detection on multiple cores inside embedded system (NVIDIA’s Drive PX2 platform)

## Object Detection History

### Viola-Jones Algorithm (2001)
Efficient Algorithm for face detection
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

### Regions with Convolutional Neural Networks (Deep RCNNs) (2015)
RCNN creates bounding boxes, or regional proposals, using a process called **Selective Search**
At a higher level, Selective search looks at the image through windows of different sizes (randomly sized and placed windows at first), and then, for each size it tries to group together adjacent pixels by texture, color, or intensity to identify objects.
