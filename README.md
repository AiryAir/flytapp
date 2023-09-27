# FlytApp
FlytApp, is a webapp  designed for the precise detection of intruders within drone footage, using the capabilities of the YOLOv8 model. This documentation serves as a guide to using FlytApp, ensuring its effective utilization.

# Index
* Tech Stack
* Features
* Dataset Description
* Authors
* License

# Tech Stack 
* Programming Languages:
    * Python: Used for the core application logic and machine learning components.
* Machine Learning and Computer Vision Libraries:
    * OpenCV: Used for image and video processing.
    * YOLO (You Only Look Once): The YOLOv8 model for object detection.
    * Ultralytics: A framework for computer vision tasks, including object detection.
* User Interface:
    * HTML, CSS: For building the frontend interface.
* Backend and Server:
    * Flask: A micro web framework for Python.
* APIs:
    * Google Maps API: Integrated for location and mapping features.
* IDE Used: Google Colab, VSCode

# Features
FlytApp offers the following key features:

* Intruder Detection: FlytApp leverages the YOLOv8 model to accurately detect intruders within drone footage.
* Real-Time Alerts: FlytApp provides real-time alerts, ensuring immediate notification of intruder detection events.
* User-Friendly Interface: FlytApp offers an intuitive and user-friendly interface, simplifying navigation and configuration for users.
* Google Maps Integration: FlytApp has seamlessly integrated Google Maps for enhanced performance, allowing for precise location tracking and mapping 
  features in real-time intruder detection scenarios. This integration enhances the application's capabilities for better situational awareness.
  
# Dataset Description
* Dataset Name: NTUT 4K Drone Photo Dataset for Human Detection
* Source: Kaggle
* Author: Kuanting Lai
* Dataset Link: [NTUT 4K Drone Photo Dataset](https://www.kaggle.com/datasets/kuantinglai/ntut-4k-drone-photo-dataset-for-human-detection/data)

  * Dataset Segmentation: We systematically divided our dataset into three subsets to ensure rigorous evaluation of our YOLOv8 model's performance. These 
    subsets include:
    - A training set consisting of 11 images.
    - A testing set containing 2 images.
    - A validation set comprising 3 images.
  * Annotation with Roboflow: To streamline the annotation process, we utilized the Roboflow platform. This platform facilitated the efficient annotation of 
    objects of interest within our dataset, optimizing our intruder detection task.
  * YOLOv8-Compatible Annotations: The annotations produced were converted into a format compatible with the YOLOv8 model, ensuring seamless integration 
    into our detection pipeline.
  * Model Training: Our YOLOv8 model was subsequently trained using this annotated dataset. This training process equipped the model with the capability to 
    effectively identify intruders within drone footage.

# Authors
* [@prathamtalekar](https://www.linkedin.com/in/air72/)
* [@adityarane](https://www.linkedin.com/in/aditya-rane-802098140/)
* [@sadhanasharma](https://www.linkedin.com/in/sadhana-sharma-/)

# License
[Apache License 2.0]()


