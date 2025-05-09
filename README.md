# 🦴 BoneScan AI: X-ray Bone Fracture Detection App

BoneScan AI is a deep learning-powered web application for detecting bone fractures from X-ray images. It uses a Convolutional Neural Network (CNN) model with Streamlit to provide real-time fracture predictions through a simple, intuitive browser interface.

---

## 📖 About

Medical imaging diagnostics, especially fracture detection, often requires expert analysis and is prone to human error under high workload conditions. BoneScan AI aims to assist radiologists and healthcare professionals by providing an AI-driven decision support system to detect potential fractures in X-ray images.

This project showcases how AI and deep learning can be integrated into accessible, real-time applications to enhance healthcare workflows.

---

## 🎯 Project Motivation

- To build an accessible AI tool for early fracture detection.
- To showcase how computer vision and deep learning can assist medical diagnostics.
- To demonstrate deploying AI models through a user-friendly web app.
- To contribute towards AI-based healthcare assistive systems.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **TensorFlow / Keras** – for model creation and inference
- **Streamlit** – for interactive web app interface
- **NumPy** – for numerical operations
- **Pillow (PIL)** – for image processing

---

## 🚀 Features

- 📥 Upload X-ray images in `.jpg`, `.jpeg`, or `.png` formats.
- 🖼️ Converts images to grayscale and resizes them to `224x224` pixels.
- 🤖 Predicts whether a bone fracture is present using a trained CNN model.
- 📊 Displays prediction results instantly in a clean, web-based interface.
- 💻 Can be deployed locally or on cloud platforms like **Streamlit Cloud**.

---

## 📊 Model Overview

- **Input:** Grayscale X-ray image (224x224 pixels)
- **Architecture:** Convolutional Neural Network (CNN)
- **Output:** Binary Classification
  - `Fracture`
  - `No Fracture`
- **Framework:** TensorFlow / Keras

---

## 🔍 Workflow

1. **Image Upload:** User uploads an X-ray image.
2. **Preprocessing:**
   - Convert to grayscale.
   - Resize to `224x224` pixels.
   - Normalize pixel values.
   - Expand dimensions to fit the CNN model input.
3. **Prediction:** Pass the processed image to the CNN model.
4. **Result Display:** Show prediction result as either **Fracture** or **No Fracture**.

---

## 📦 Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/bone-fracture-detector.git
cd bone-fracture-detector

```
Install dependencies:

```bash

pip install -r requirements.txt
```
Run the app:

```bash

streamlit run app.py
```
📸 Demo
Upload an X-ray image
Click Predict
Get instant result: Fracture / No Fracture


📈 Results & Performance
Metric	Value
Training Accuracy	98%
Validation Accuracy	95%
Test Accuracy	94%
Inference Time	~1 second/image

Note: Values based on internal dataset used during model training.

⚠️ Limitations
Not a replacement for professional medical diagnosis.

Accuracy dependent on the quality and variety of X-ray images.

Model trained on a limited dataset — requires further data augmentation for broader use.

Currently supports binary classification only (Fracture / No Fracture).




🤝 Contribution Guidelines
Contributions are welcome!
To contribute:

Fork this repository.

Create a new branch (git checkout -b feature-name).

Make your changes and commit them.

Push to your branch (git push origin feature-name).

Create a Pull Request.

📧 Contact
A.M. Mukilan
GitHub: MUKILAN0608

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.


---

