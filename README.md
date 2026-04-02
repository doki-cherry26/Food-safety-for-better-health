🍽️ Food Safety for Better Health
📌 Project Overview

Food Safety for Better Health is an AI-powered web application that identifies food items from images and provides nutritional insights along with health recommendations.

The system leverages Deep Learning models (CNN, VGG16, ResNet50) and integrates Redis database to deliver fast predictions, model performance metrics, and nutrient information in real time.

🎯 Objective

To build an intelligent system that:

Classifies food images into predefined categories
Provides detailed nutritional values
Displays model evaluation metrics
Offers doctor recommendations based on health factors
🧠 Models Used
Custom CNN
VGG16 (Transfer Learning)
ResNet50 (Transfer Learning)

Each model was trained and evaluated to compare performance.

📊 Dataset Details
Total Classes: 34 Food Categories
Training Images: 200 per class
Validation Images: 50 per class
Testing Images: 10 per class
🍕 Classes Include:

apple_pie, baked_potato, burger, butter_naan, chai, chapathi,
cheesecake, chicken_curry, chole_bhature, crispy_chicken,
dal_makhani, dhokla, donut, fried_rice, french_fries, hot_dog,
ice_cream, idli, jalebi, kaathi_roll, kadai_paneer, kulfi,
masala_dosa, momos, omelette, pani_puri, pakode, pav_bhaji,
pizza, samosa, sandwich, sushi, taco, taquito

🧪 Model Evaluation Metrics

The system stores and displays:

✅ Accuracy
✅ Precision
✅ Recall
✅ F1-Score
✅ Confusion Matrix

Metrics are dynamically fetched from Redis.

🥗 Nutritional Information

Each food item includes:

Calories (kcal)
Total Fat, Saturated Fat, Trans Fat
Cholesterol
Sodium
Carbohydrates & Fiber
Sugar
Protein
Vitamins & Minerals (Vitamin C, Calcium, Iron, Potassium)
🩺 Doctor Recommendation Logic

Based on:

Calories
Fat content
Output:
✅ Recommended for consumption
❌ Not recommended frequently
⚙️ Tech Stack
🔹 Backend
Python
Flask
TensorFlow / Keras
🔹 Frontend
HTML
CSS
🔹 Database
Redis (for storing):
Model metrics
Nutritional data
🔹 Tools
Google Colab (Model Training)
PyCharm (Development)
🔄 Workflow
Upload food image
Select model (CNN / VGG16 / ResNet50)
Model predicts food class
Fetch:
Prediction confidence
Evaluation metrics from Redis
Nutritional data from Redis
Display:
Results
Confusion matrix
Health recommendation
🚀 Features
📸 Image-based food classification
🤖 Multiple model comparison
⚡ Fast retrieval using Redis
📊 Real-time performance metrics
🥗 Nutritional insights
🩺 Health recommendation system
🌐 Interactive web interface
📁 Project Structure
project/
│── models/
│   ├── CNN_model.h5
│   ├── resnet_model.h5
│   ├── vgg16_model.h5
│
│── static/
│   └── uploads/
│
│── templates/
│   └── index.html
│
│── app.py
│── nutrients.json
│── README.md
📸 Output Screens
Image Upload Interface
Model Selection
Prediction Result
Metrics Dashboard
Nutritional Information
Doctor Recommendation
📈 Future Improvements
Increase dataset size for better accuracy
Add more food categories
Deploy on cloud (AWS / Azure)
Mobile application integration
Real-time camera detection

⭐ Acknowledgements
TensorFlow & Keras
Redis
Open-source datasets
Google Colab

## 📌 Conclusion

**Food Safety for Better Health** showcases how Deep Learning can be used to classify food images and provide real-time nutritional insights with health recommendations. By combining multiple models (CNN, VGG16, ResNet50) with Redis for fast data retrieval, the system delivers an efficient and practical solution for promoting healthier food choices.


👩‍💻 Author
Charishma Doki
AI&ML INTERN

