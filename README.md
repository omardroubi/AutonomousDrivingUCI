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
