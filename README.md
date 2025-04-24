
---

# 🗑️ Garbage Detection using YOLOv11

## Overview

This project presents an **AI-powered Garbage Detection System** using **YOLOv11**, the latest real-time object detection architecture from Ultralytics. The system is designed to accurately identify and locate garbage in various environments, helping in smart city management, cleanliness monitoring, and environmental awareness applications.

---

## 🚀 Features

- **Real-time Detection** – Fast and accurate detection of garbage objects in images or video streams.
- **Custom Trained Model** – Fine-tuned on a specialized garbage dataset for high precision.
- **Scalable** – Easily deployable across drones, surveillance cameras, and mobile apps.
- **Flexible Input** – Supports image files, video streams, webcams, and IP cameras.
- **Open Source** – Encourages collaboration and further development by the community.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ramsha-18/garbage-detection.git
cd garbage-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Model Weights

Place your trained `best.pt` model in the root directory or models folder.

---

## 🧪 Inference

### Command Line

```bash
yolo predict model=best.pt source='path/to/image_or_video'
```

### Python Usage

```python
from ultralytics import YOLO
import cv2

# Load model
model = YOLO('best.pt')

# Open video or webcam
cap = cv2.VideoCapture(0)  # or path to video file

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()
    cv2.imshow('Garbage Detection', annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 🧠 Training

### Dataset Preparation

Ensure your garbage dataset is annotated in YOLO format and structured as follows:

```
dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
├── dataset.yaml
```

### Train the Model

```bash
yolo train model=yolov11.yaml data=dataset.yaml epochs=100 imgsz=640
```

---

## 📂 Project Structure

```
garbage-detection/
├── models/
│   └── best.pt
├── dataset/
├── runs/
├── detect.py
├── train.py
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! You can:
- Fork the repo and submit a PR
- Open issues for bugs or feature requests
- Suggest improvements and integrations

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

Special thanks to **Ultralytics** for their incredible work on YOLO models.  
YOLOv11 builds on a foundation of continual improvements in speed and accuracy for real-time object detection.

---

