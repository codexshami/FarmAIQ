from flask import Flask, render_template, request
from markupsafe import Markup
import numpy as np
import pandas as pd
import pickle
import io
import torch
from torchvision import transforms
from PIL import Image
import os

from utils.model import ResNet9
from utils.fertilizer import fertilizer_dic
from utils.disease import disease_dic

app = Flask(__name__)

# Ensure templates folder is in the correct location
app.template_folder = 'templates'
app.static_folder = 'static'

# ---------------- LOAD MODELS ----------------

# Load crop recommendation model
crop_model = pickle.load(open("RandomForest.pkl", "rb"))

# Load disease classes and model
disease_classes = list(disease_dic.keys())
disease_model = ResNet9(3, len(disease_classes))
disease_model.load_state_dict(torch.load("plant_disease_model.pth", map_location="cpu"))
disease_model.eval()

print("✅ All models loaded successfully!")

# ---------------- IMAGE PREDICT ----------------

def predict_image(img):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    image = Image.open(io.BytesIO(img)).convert('RGB')
    img_t = transform(image)
    img_t = torch.unsqueeze(img_t, 0)

    with torch.no_grad():
        outputs = disease_model(img_t)
        _, preds = torch.max(outputs, 1)
    
    return disease_classes[preds[0].item()]

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    """Home page"""
    return render_template("index.html")

# ---------------- CROP RECOMMENDATION ----------------

@app.route("/crop_recommend")
def crop_recommend():
    """Crop recommendation form"""
    return render_template("crop.html")

@app.route("/crop-result", methods=["POST"])
def crop_predict():
    """Crop prediction result"""
    try:
        N = int(request.form["nitrogen"])
        P = int(request.form["phosphorous"])
        K = int(request.form["pottasium"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Fixed data array - temperature and humidity values were hardcoded
        data = np.array([[N, P, K, ph, rainfall, 30, 80]])  # [N,P,K,temp,humidity,pH,rainfall]

        prediction = crop_model.predict(data)[0]
        
        return render_template("crop-result.html", prediction=prediction.title())
    
    except Exception as e:
        return render_template("crop-result.html", prediction="Error in prediction. Please check your inputs.")

# ---------------- FERTILIZER RECOMMENDATION ----------------

@app.route("/fertilizer_recommendation")
def fertilizer():
    """Fertilizer recommendation form"""
    return render_template("fertilizer.html")

@app.route("/fertilizer-predict", methods=["POST"])
def fertilizer_predict():
    """Fertilizer prediction result"""
    try:
        crop_name = request.form["cropname"]
        N = int(request.form["nitrogen"])
        P = int(request.form["phosphorous"])
        K = int(request.form["pottasium"])

        # Load fertilizer data
        df = pd.read_csv("Data/fertilizer.csv")
        
        # Get required NPK values for the crop
        nr = df[df["Crop"] == crop_name]["N"].iloc[0]
        pr = df[df["Crop"] == crop_name]["P"].iloc[0]
        kr = df[df["Crop"] == crop_name]["K"].iloc[0]

        # Calculate deficiencies
        n = nr - N
        p = pr - P
        k = kr - K

        # Determine the most deficient nutrient
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        key = temp[max(temp)]

        # Determine high/low status
        if key == "N":
            key = "NHigh" if n < 0 else "Nlow"
        elif key == "P":
            key = "PHigh" if p < 0 else "Plow"
        else:
            key = "KHigh" if k < 0 else "Klow"

        recommendation = Markup(str(fertilizer_dic[key]))
        
        return render_template("fertilizer-result.html", 
                             recommendation=recommendation,
                             crop_name=crop_name.title())
    
    except Exception as e:
        return render_template("fertilizer-result.html", 
                             recommendation=Markup("Error: Please check your inputs or crop name."))

# ---------------- DISEASE PREDICTION ----------------

@app.route("/disease_prediction", methods=["GET", "POST"])
def disease_predict():
    """Disease prediction form and result"""
    if request.method == "POST":
        try:
            if 'file' not in request.files:
                return render_template("disease.html", error="No file selected")
            
            file = request.files["file"]
            if file.filename == "":
                return render_template("disease.html", error="No file selected")
            
            if file:
                img = file.read()
                prediction = predict_image(img)
                result = Markup(str(disease_dic[prediction]))
                
                return render_template("disease-result.html", 
                                     prediction=result,
                                     disease_name=prediction.replace('_', ' ').title())
        
        except Exception as e:
            return render_template("disease.html", error=f"Error processing image: {str(e)}")
    
    return render_template("disease.html")

# ---------------- 404 HANDLER ----------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    print("🚀 Starting Precision Agriculture Flask App...")
    print("📁 Expected folder structure:")
    print("   - templates/")
    print("   - static/")
    print("   - Data/fertilizer.csv")
    print("   - RandomForest.pkl")
    print("   - plant_disease_model.pth")
    print("\n🌐 Server running on http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)