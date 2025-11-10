# 🦷 DentaScanAI – AI-Powered Dental Health Analysis

![Project Preview](assets/dentalscan_preview.png)

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-red?logo=ultralytics)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)](https://opencv.org/)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-PyTorch-orange?logo=pytorch)](https://pytorch.org/)
[![Hackathon Project](https://img.shields.io/badge/Event-MEDHA%202025%20(IIT%20Bombay)-brightgreen)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Overview

**DentaScanAI** is an AI-powered web application built to assist in **dental health analysis** through **image-based diagnosis**.  
It uses **Deep Learning (YOLOv8-L)** to detect and classify dental issues from X-ray images and integrates **real-time doctor consultation**, **AI-generated health reports**, and **clinic recommendations** — all within one platform.

This project was developed during **MEDHA-2025 (IIT Bombay Edition)** Hackathon hosted by **GL Bajaj Institute of Technology & Management**, as part of a 36-hour hackathon sprint.

---

## 🧩 Project Features

- 🧠 **AI Model (YOLOv8-L)** trained on **2400+ dental X-ray images** across **9 categories**.  
- ⚙️ **80-20 Train-Test Split** with **48 epochs** of training.  
- 📈 Achieved **~75–80% accuracy** during evaluation.  
- 🩺 **AI-Powered Diagnosis:** Detects and classifies dental conditions automatically.  
- 🧾 **AI-Generated Reports:** Summarizes detected issues and recommended next steps.  
- 👩‍⚕️ **Doctor Connect:** Real-time chat and video consultations with dentists.  
- 🏥 **Nearby Clinics:** Suggests local dental clinics for quick appointments.  
- 💬 **Home Remedies:** Offers temporary relief suggestions based on detected issue.  

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Model** | YOLOv8-L (Ultralytics) |
| **Language** | Python |
| **Libraries** | OpenCV, NumPy, Pandas, Torch, Ultralytics |
| **Frontend** | HTML, CSS, JavaScript, React (optional) |
| **Backend** | Flask / FastAPI |
| **Database** | MongoDB / Firebase |
| **Deployment** | Local Server (Hackathon Build) |
| **GPU Used** | NVIDIA GeForce RTX 3050 (6 GB) |

---

## 📊 Model Performance

| Metric | Result |
|--------|--------|
| Training Images | 2400 |
| Epochs | 48 |
| Accuracy | ~75–80% |
| Dataset Split | 80% Train / 20% Test |

---

## 🔄 Workflow

```mermaid
graph TD
A[Dataset Collection & Preprocessing] --> B[Annotation & Labeling]
B --> C[YOLOv8-L Model Training]
C --> D[Evaluation & Accuracy Testing]
D --> E[Integration with Backend API]
E --> F[Frontend Web Interface]
F --> G[Real-time Inference & User Interaction]

