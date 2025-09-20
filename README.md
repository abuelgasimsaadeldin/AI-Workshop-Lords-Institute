# IIUM AI Workshop for Lords Institute 🚀

Welcome to the **IIUM AI Workshop at Lords Institute of Engineering & Technology**!  
This repository contains all the **hands-on code, exercises, and resources** covered throughout the 10-day workshop.  

Our goal is to introduce students to **Artificial Intelligence (AI), Computer Vision, Large Language Models (LLMs), Vision Language Models (VLMs) and more!** with a mix of theory and practical coding.

---

## 📂 Repository Structure

The repository is organized by **days**. Each day has its own folder containing Jupyter notebooks, scripts, and supporting files.

```
AI-Workshop-Lords-Institute/
│
├── Day1_Introduction_Env_PyTorch_OpenCV/
├── Day2_Image_Classification/
├── Day3_Object_Detection_YOLO/
├── Day4_Object_Detection_Applications/
├── Day5_LLMs_HuggingFace_VLMs/
├── Day8_Foundation_VLM_Autolabeling/
├── Day9_Model_Deployment_Git/
├── Day10_3D_CAD_Drawing/
├── Day11_3D_Printing/
└── Day12_Conclusion/
```


---

## 📅 Workshop Schedule & Contents

### **Day 1: Introduction & Environment Setup**
- Ice breaking activity
- Installation: Miniconda + VSCode
- Python essentials: numpy, pandas
- Intro to PyTorch (Jupyter Notebook)
- Intro to OpenCV (images, videos, face detection using Haar Cascades)

### **Day 2: Image Classification**
- CNNs, pretrained models, finetuning
- Running on Google Colab
- GUI for image classification (Tkinter)

### **Day 3: Object Detection with YOLO**
- YOLO inference on images/videos
- Data annotation & labeling
- Model finetuning
- Assignment: GUI for YOLO inference

### **Day 4: Applications of Object Detection**
- Real-world case studies (waste detection, traffic, safety monitoring)
- Hands-on 1: Waste detection  
- Hands-on 2: Vehicle & pedestrian counting

### **Day 5: Large Language Models (LLMs)**
- Introduction to LLMs
- Hugging Face ecosystem
- Intro to Vision-Language Models (VLMs)

### **Day 8: Advanced Vision Models**
- Foundation VLMs for enhancing YOLO
- Auto-labeling & Autodistill

### **Day 9: Model Deployment & Git**
- Git essentials (clone, commit, push, pull)
- Coding standards: DRY, KISS
- Deployment workflows

### **Day 10: 3D CAD Drawing**
- Basics of 3D design
- Hands-on CAD exercises

### **Day 11: 3D Printing**
- Introduction to 3D printing technology
- Printing from CAD models

### **Day 12: Conclusion**
- Recap of all modules
- Closing ceremony

---

## 🛠️ Requirements

- Python 3.9+
- Miniconda
- Jupyter Notebook / Google Colab
- Required libraries (install via `requirements.txt`):

```
numpy
pandas
torch
torchvision
opencv-python
matplotlib
ultralytics
transformers
huggingface_hub
```


> 📌 Each day’s folder may include an additional `requirements.txt` for that specific module.

---

## 🚀 Getting Started

1. Clone the repo:
 ```bash
 git clone https://github.com/abuelgasimsaadeldin/AI-Workshop-Lords-Institute.git
 cd AI-Workshop-Lords-Institute
```

2. Create and activate a conda environment:
```
conda create -n aiworkshop python=3.9
conda activate aiworkshop
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Navigate to the desired day’s folder and run the notebooks/scripts.
