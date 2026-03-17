<p align="center">
  
# 🌱 **Smart Agriculture Recommendation System** 
### *Empowering Farmers with AI-Driven Insights for Sustainable Farming*

</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9C34&center=true&vCenter=true&width=600&lines=🌾+Intelligent+Crop+Recommendations;🧪+Smart+Fertilizer+Advisory;🍃+AI-Powered+Disease+Detection;📊+Data-Driven+Agriculture;🤖+Machine+Learning+for+Farming" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest%20%7C%20CNN-green?style=for-the-badge&logo=scikit-learn" alt="ML">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Dataset-Kaggle-orange?style=for-the-badge&logo=kaggle" alt="Kaggle">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge" alt="Contributions">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=Smart%20Agriculture%20ML&fontSize=50&fontAlignY=35&animation=twinkling&fontColor=white"/>
</p>

---

<p align="center">
  
## 📋 **Table of Contents**

</p> 

- [ Overview](#-overview)
- [ Key Features](#-key-features)
- [ Data Sources](#-data-sources)
- [ Machine Learning Models](#-machine-learning-models)
- [ System Architecture](#-system-architecture)
- [ Application Screenshots](#-application-screenshots)
- [ Technologies Used](#️-technologies-used)
- [ Project Structure](#-project-structure)
- [ Installation Guide](#️-installation-guide)
- [ How to Use](#-how-to-use)
- [ Performance Metrics](#-performance-metrics)
- [ Future Enhancements](#-future-enhancements)
- [ Contributors](#-contributors)
- [ License](#-license)
- [ Contact & Support](#-contact--support)

---

<p align="center">

## 🌟 **Overview**

</p>

Welcome to the **Smart Agriculture Recommendation System** – a cutting-edge Machine Learning solution designed to revolutionize traditional farming practices! This comprehensive system combines **crop recommendation**, **fertilizer advisory**, and **plant disease detection** to provide farmers with a complete agricultural decision support tool.

> *"Transforming Indian Agriculture through Artificial Intelligence - One Farm at a Time"*

<p align="center">
  
### 🎯 **Problem Statement**

</p>

Indian farmers face multiple challenges in modern agriculture:
- ❌ **Low Crop Yield** - Due to improper crop selection
- ❌ **Soil Degradation** - From incorrect fertilizer usage
- ❌ **Crop Diseases** - Late detection leading to massive losses
- ❌ **Financial Losses** - Poor decisions affecting livelihood
- ❌ **Knowledge Gap** - Limited access to agricultural expertise

<p align="center">
  
### 💡 **Our Solution**

</p>

An intelligent multi-modal recommendation engine that:

| Feature | Solution | Impact |
|---------|----------|--------|
| **🌾 Crop Recommendation** | ML-based crop selection | 30% yield increase |
| **🧪 Fertilizer Advisory** | Nutrient deficiency analysis | 25% cost reduction |
| **🍃 Disease Detection** | Deep learning image analysis | 40% loss prevention |

---
<p align="center">
  
## ✨ **Key Features**

</p>

<p align="center">
  <img src="images/features_animation.gif" alt="Features Animation" width="600px">
</p>

### **🌾 Crop Recommendation Module**
- ✅ Analyzes soil composition (N, P, K levels)
- ✅ Considers environmental factors (temperature, humidity, pH, rainfall)
- ✅ Recommends from **22 different crops**
- ✅ Provides detailed crop information and cultivation tips

### **🧪 Fertilizer Advisory Module**
- ✅ Identifies nutrient deficiencies in soil
- ✅ Suggests optimal fertilizers with dosage
- ✅ Covers **7 types of fertilizers**
- ✅ Provides application guidelines

### **🍃 Plant Disease Detection Module**
- ✅ Deep Learning-based image recognition
- ✅ Identifies **38 different plant diseases**
- ✅ Supports **14 crop species**
- ✅ Provides treatment recommendations
- ✅ Instant diagnosis within seconds

---
<p align="center">
  
## 📊 **Data Sources**

</p>

Our system leverages high-quality datasets from trusted sources to ensure accurate predictions.

### **1. Crop Recommendation Dataset** 📈
- **Source**: [Kaggle - Crop Recommendation Dataset](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)
- **Description**: Custom built dataset containing soil and environmental parameters for 22 crops
- **Features**: Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall
- **Samples**: 2,200 records
- **Crops**: Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee

### **2. Fertilizer Suggestion Dataset** 🧪
- **Source**: [GitHub - Harvestify Dataset](https://github.com/Gladiator07/Harvestify/blob/master/Data-processed/fertilizer.csv)
- **Description**: Custom built dataset for fertilizer recommendations based on NPK values
- **Features**: Nitrogen, Phosphorus, Potassium, Soil Type, Crop Type
- **Fertilizers Covered**: Urea, DAP, MOP, 10-26-26, 28-28, 17-17-17, 20-20, Sulphur

### **3. Plant Disease Detection Dataset** 🍃
- **Source**: [Kaggle - New Plant Diseases Dataset](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset)
- **Description**: Large-scale dataset of plant leaf images for disease classification
- **Total Images**: 87,000+ RGB images
- **Categories**: 38 disease classes + healthy classes
- **Crops Covered**: 
  - 🍅 Tomato (10 diseases)
  - 🥔 Potato (3 diseases)
  - 🌶️ Pepper (2 diseases)
  - 🍏 Apple (4 diseases)
  - 🍇 Grape (4 diseases)
  - 🍊 Citrus (4 diseases)
  - 🍓 Strawberry (2 diseases)
  - 🎃 Squash (2 diseases)
  - 🍑 Peach (2 diseases)
  - 🍒 Cherry (2 diseases)
  - 🌽 Corn (4 diseases)
  - 🫘 Blueberry (1 disease)
  - 🍐 Pear (1 disease)
  - Raspberry (1 disease)
  - Soybean (1 disease)

---
<p align="center">


  
## 🧠 **Machine Learning Models**

</p>


### **Model 1: Crop Recommendation - Random Forest Classifier**

<p align="center">
  <img src="images/rf_visualization.png" alt="Random Forest Visualization" width="500px">
</p>
<p align="center">
  
#### **Architecture**

</p>

- **Algorithm**: Random Forest Classifier
- **Number of Trees**: 100
- **Max Depth**: 10
- **Criterion**: Gini Impurity
- **Cross-Validation**: 5-fold

<p align="center">
  
#### **Input Parameters**

</p>

| Parameter | Description | Range |
|-----------|-------------|-------|
| **Nitrogen (N)** | Essential for leaf growth | 0-140 kg/ha |
| **Phosphorus (P)** | Root development promoter | 0-145 kg/ha |
| **Potassium (K)** | Overall plant health | 0-205 kg/ha |
| **Temperature** | Atmospheric temperature | 8-45°C |
| **Humidity** | Relative humidity | 14-100% |
| **pH Value** | Soil acidity/alkalinity | 3.5-10 |
| **Rainfall** | Annual precipitation | 20-300 mm |

### **Model 2: Disease Detection - Convolutional Neural Network (CNN)**

<p align="center">
  <img src="images/cnn_architecture.png" alt="CNN Architecture" width="700px">
</p>
<p align="center">
  
#### **Architecture Details**

</p>

Input Layer (224x224x3)
↓
Conv2D (32 filters, 3x3, ReLU) + MaxPooling (2x2)
↓
Conv2D (64 filters, 3x3, ReLU) + MaxPooling (2x2)
↓
Conv2D (128 filters, 3x3, ReLU) + MaxPooling (2x2)
↓
Conv2D (256 filters, 3x3, ReLU) + MaxPooling (2x2)
↓
Flatten
↓
Dense (512, ReLU) + Dropout (0.5)
↓
Dense (256, ReLU) + Dropout (0.3)
↓
Output Layer (38 classes, Softmax)

#### **Training Configuration**
- **Optimizer**: Adam (learning rate = 0.001)
- **Loss Function**: Categorical Crossentropy
- **Batch Size**: 32
- **Epochs**: 50
- **Validation Split**: 20%
- **Data Augmentation**: Rotation, Zoom, Flip, Shift

---

## 📊 **System Architecture**

<p align="center">
  <img src="images/system_architecture.png" alt="System Architecture" width="900px">
  <br>
  <em>Figure 1: Complete System Architecture with Three Modules</em>
</p>


---

## 📸 **Application Screenshots**

### **🏠 Home Page - Main Dashboard**
<p align="center">
  <img src="images/home_dashboard.png" alt="Home Dashboard" width="900px">
  <br>
  <em>Figure 2: Smart Agriculture Dashboard - Main Interface with Navigation</em>
</p>

### **🌾 Crop Recommendation Module**
<p align="center">
  <img src="images/crop_input.png" alt="Crop Input Form" width="450px">
  <img src="images/crop_result.png" alt="Crop Result" width="450px">
  <br>
  <em>Figure 3: Crop Recommendation - Input Form and Results</em>
</p>

### **🧪 Fertilizer Advisory Module**
<p align="center">
  <img src="images/fertilizer_input.png" alt="Fertilizer Input" width="450px">
  <img src="images/fertilizer_result.png" alt="Fertilizer Result" width="450px">
  <br>
  <em>Figure 4: Fertilizer Advisory - NPK Analysis and Recommendations</em>
</p>

### **🍃 Plant Disease Detection Module**
<p align="center">
  <img src="images/disease_upload.png" alt="Disease Upload" width="450px">
  <img src="images/disease_result.png" alt="Disease Result" width="450px">
  <br>
  <em>Figure 5: Disease Detection - Image Upload and Diagnosis Results</em>
</p>

### **📊 Analytics Dashboard**
<p align="center">
  <img src="images/analytics_1.png" alt="Analytics 1" width="450px">
  <img src="images/analytics_2.png" alt="Analytics 2" width="450px">
  <br>
  <em>Figure 6: Analytics Dashboard - Data Visualization and Insights</em>
</p>

### **📱 Mobile Responsive Views**
<p align="center">
  <img src="images/mobile_1.png" alt="Mobile View 1" width="250px">
  <img src="images/mobile_2.png" alt="Mobile View 2" width="250px">
  <img src="images/mobile_3.png" alt="Mobile View 3" width="250px">
  <br>
  <em>Figure 7: Mobile-Responsive Interface on Different Devices</em>
</p>

### **📈 Model Performance Charts**
<p align="center">
  <img src="images/accuracy_chart.png" alt="Accuracy Chart" width="450px">
  <img src="images/confusion_matrix.png" alt="Confusion Matrix" width="450px">
  <br>
  <em>Figure 8: Model Performance Metrics and Confusion Matrix</em>
</p>

### **🌍 Regional Language Support**
<p align="center">
  <img src="images/hindi_interface.png" alt="Hindi Interface" width="450px">
  <img src="images/tamil_interface.png" alt="Tamil Interface" width="450px">
  <br>
  <em>Figure 9: Multi-language Support for Regional Farmers</em>
</p>

---

## 🛠️ **Technologies Used**

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,tensorflow,keras,sklearn,streamlit,pandas,numpy,matplotlib,seaborn,flask,git,github,vscode,html,css" />
</p>

| Category | Technology | Purpose |
|----------|------------|---------|
| **Core Language** | Python 3.8+ | Primary programming language |
| **Web Framework** | Streamlit | Interactive web application |
| **Machine Learning** | Scikit-learn | Random Forest, Preprocessing |
| **Deep Learning** | TensorFlow, Keras | CNN for disease detection |
| **Data Processing** | Pandas, NumPy | Data manipulation and analysis |
| **Visualization** | Matplotlib, Seaborn, Plotly | Charts and graphs |
| **Image Processing** | OpenCV, PIL | Image preprocessing |
| **Model Serialization** | Joblib, Pickle | Save/load trained models |
| **Version Control** | Git, GitHub | Code management |
| **Deployment** | Streamlit Cloud, Heroku | Web hosting |
| **Development** | VS Code, Jupyter | IDE and notebooks |

### **Key Libraries with Versions**
```python
tensorflow==2.13.0
keras==2.13.1
scikit-learn==1.3.0
streamlit==1.25.0
pandas==2.0.3
numpy==1.24.3
opencv-python==4.8.0
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.15.0
Pillow==10.0.0
joblib==1.3.1

```
### Disease Detection Example:

📥 INPUT: [Image of tomato leaf with spots]

📤 OUTPUT:
🍃 Disease: Tomato Late Blight
📊 Confidence: 96.2%
🔍 Symptoms: Dark lesions on leaves, white mold on undersides
💊 Treatment:
  • Organic: Copper spray, neem oil
  • Chemical: Mancozeb, Chlorothalonil
⚠️ Prevention: Crop rotation, resistant varieties

### Intallation 

git clone https://github.com/codexshami/FarmAIQ.git && cd FarmAIQ && python -m venv venv && (venv\Scripts\activate || source venv/bin/activate) && pip install -r requirements.txt && streamlit run app.py
