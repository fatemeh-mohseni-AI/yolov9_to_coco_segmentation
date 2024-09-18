# YOLOv9 to COCO Conversion for Instance Segmentation

This repository contains code to convert YOLOv9 instance segmentation annotations into COCO format. The dataset used in this project includes categories related to chicken health and manure conditions for analysis and segmentation.
# Project Overview

In this project, we convert YOLOv9 format annotations (which include bounding boxes and polygon points for instance segmentation) to COCO format.

# Dataset

place your own categories:

# Installation

To run the conversion script, you need to install the following dependencies:


```
pip install opencv-python json
```


# Usage

To convert YOLOv9 annotations into COCO format, follow these steps:

>    Clone this repository:

>    bash
```
git clone https://github.com/yourusername/yolo-to-coco-conversion.git
```

# Prepare your YOLO annotations and images in the following folder structure:


```
dataset/
    ├── annotations/
    │    ├── image1.txt
    │    └── image2.txt
    └── images/
         ├── image1.jpg
         └── image2.jpg
```

# Run the conversion script:


```
    python convert_yolo_to_coco.py
```
# Example Output

The generated COCO file will follow the standard COCO format structure, including images, annotations, and categories. Here is an example of the annotation section:
```
{
  "annotations": [
    {
      "id": 1,
      "image_id": 1,
      "category_id": 1,
      "bbox": [100.5, 200.3, 50.5, 70.2],
      "segmentation": [[100, 200, 150, 210, ...]],
      "area": 3551.0,
      "iscrowd": 0
    }
  ]
}
```
