# dental_detection

# 🦷 Dental Disease Detection using YOLOv8

This project focuses on detecting and classifying **dental diseases** using **Computer Vision and Deep Learning**. It leverages the **Ultralytics YOLOv8** model to identify various dental issues from X-ray images, aiming to assist dental professionals with AI-powered diagnosis.

---


## 🔍 Project Overview

This project explores the potential of **AI in medical imaging**, specifically dental X-rays. Using a custom dataset of **8105 images**, the model was trained to detect and classify multiple dental conditions with high precision and speed.


---

## 🧩 Dataset Details

Total images: **8105**  
- 📂 **6484** images for training  
- 📁 **1621** images for validation/testing  

The dataset includes labeled images of various dental conditions such as:  
🦷 Cavities 🦷 Plaque 🦷 Tooth Fractures 🦷 Root Infection 🦷 Gum Disease  

*(You can modify or expand the categories based on your dataset.)*

---

## ⚙️ Technical Details

- **Framework:** Ultralytics YOLOv8L  
- **Language:** Python  
- **Libraries:** OpenCV, NumPy, Ultralytics, Torch  
- **GPU:** NVIDIA GeForce RTX 3050 (6 GB)  
- **Training Duration:** ~2 days  

---

## 📊 Validation Results

| Metric | Score |
|--------|-------|
| 🏁 mAP50 (for main class) | **0.753** |
| 📈 Overall mAP50-95 | **0.576** |
| ⚡ Speed | **0.3 ms preprocess | 40.4 ms inference per image** |

---

## 🧠 Model Workflow

```mermaid
graph TD
A[Data Collection] --> B[Data Preprocessing]
B --> C[Annotation and Labeling]
C --> D[Model Training using YOLOv8L]
D --> E[Validation & Testing]
E --> F[Real-time Inference System]
F --> G[Result Visualization & API Integration]
