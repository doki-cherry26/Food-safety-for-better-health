
<h1>🍽️ Food Safety for Better Health</h1>

<div class="section box">
<h2>📌 Project Overview</h2>
<p>
Food Safety for Better Health is an AI-powered web application that identifies food items from images and provides nutritional insights along with health recommendations.
</p>
<p>
The system leverages Deep Learning models (CNN, VGG16, ResNet50) and integrates Redis database to deliver fast predictions, model performance metrics, and nutrient information in real time.
</p>
</div>

<div class="section box">
<h2>🎯 Objective</h2>
<ul>
<li>Classifies food images into predefined categories</li>
<li>Provides detailed nutritional values</li>
<li>Displays model evaluation metrics</li>
<li>Offers doctor recommendations based on health factors</li>
</ul>
</div>

<div class="section box">
<h2>🧠 Models Used</h2>
<ul>
<li>Custom CNN</li>
<li>VGG16 (Transfer Learning)</li>
<li>ResNet50 (Transfer Learning)</li>
</ul>
</div>

<div class="section box">
<h2>📊 Dataset Details</h2>
<p><b>Total Classes:</b> 34 Food Categories</p>
<p><b>Training Images:</b> 200 per class</p>
<p><b>Validation Images:</b> 50 per class</p>
<p><b>Testing Images:</b> 10 per class</p>
</div>

<div class="section box">
<h2>🍕 Classes Include</h2>
<p>
apple_pie, baked_potato, burger, butter_naan, chai, chapathi, cheesecake,
chicken_curry, chole_bhature, crispy_chicken, dal_makhani, dhokla, donut,
fried_rice, french_fries, hot_dog, ice_cream, idli, jalebi, kaathi_roll,
kadai_paneer, kulfi, masala_dosa, momos, omelette, pani_puri, pakode,
pav_bhaji, pizza, samosa, sandwich, sushi, taco, taquito
</p>
</div>

<div class="section box">
<h2>🧪 Model Evaluation Metrics</h2>
<ul>
<li>Accuracy</li>
<li>Precision</li>
<li>Recall</li>
<li>F1-Score</li>
<li>Confusion Matrix</li>
</ul>
<p>Metrics are dynamically fetched from Redis.</p>
</div>

<div class="section box">
<h2>🥗 Nutritional Information</h2>
<ul>
<li>Calories (kcal)</li>
<li>Total Fat, Saturated Fat, Trans Fat</li>
<li>Cholesterol</li>
<li>Sodium</li>
<li>Carbohydrates & Fiber</li>
<li>Sugar</li>
<li>Protein</li>
<li>Vitamins & Minerals (Vitamin C, Calcium, Iron, Potassium)</li>
</ul>
</div>

<div class="section box">
<h2>🩺 Doctor Recommendation Logic</h2>
<p><b>Based on:</b></p>
<ul>
<li>Calories</li>
<li>Fat content</li>
</ul>
<p>
✅ Recommended for consumption <br>
❌ Not recommended frequently
</p>
</div>

<div class="section box">
<h2>⚙️ Tech Stack</h2>

<h3>Backend</h3>
<ul>
<li>Python</li>
<li>Flask</li>
<li>TensorFlow / Keras</li>
</ul>

<h3>Frontend</h3>
<ul>
<li>HTML</li>
<li>CSS</li>
</ul>

<h3>Database</h3>
<ul>
<li>Redis (Model metrics, Nutritional data)</li>
</ul>

<h3>Tools</h3>
<ul>
<li>Google Colab</li>
<li>PyCharm</li>
</ul>

</div>

<div class="section box">
<h2>🔄 Workflow</h2>
<ol>
<li>Upload food image</li>
<li>Select model (CNN / VGG16 / ResNet50)</li>
<li>Model predicts food class</li>
<li>Fetch prediction confidence, metrics, and nutrients</li>
<li>Display results, confusion matrix, and health recommendation</li>
</ol>
</div>

<div class="section box">
<h2>🚀 Features</h2>
<ul>
<li>Image-based food classification</li>
<li>Multiple model comparison</li>
<li>Fast retrieval using Redis</li>
<li>Real-time performance metrics</li>
<li>Nutritional insights</li>
<li>Health recommendation system</li>
<li>Interactive web interface</li>
</ul>
</div>

<div class="section box">
<h2>📁 Project Structure</h2>
<pre>
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
</pre>
</div>

<div class="section box">
<h2>📸 Output Screens</h2>
<ul>
<li>Image Upload Interface</li>
<li>Model Selection</li>
<li>Prediction Result</li>
<li>Metrics Dashboard</li>
<li>Nutritional Information</li>
<li>Doctor Recommendation</li>
</ul>
</div>

<div class="section box">
<h2>📈 Future Improvements</h2>
<ul>
<li>Increase dataset size for better accuracy</li>
<li>Add more food categories</li>
<li>Deploy on cloud (AWS / Azure)</li>
<li>Mobile application integration</li>
<li>Real-time camera detection</li>
</ul>
</div>

<div class="section box">
<h2>⭐ Acknowledgements</h2>
<ul>
<li>TensorFlow & Keras</li>
<li>Redis</li>
<li>Open-source datasets</li>
<li>Google Colab</li>
</ul>
</div>

<div class="section box">
<h2>📌 Conclusion</h2>
<p>
Food Safety for Better Health showcases how Deep Learning can be used to classify food images and provide real-time nutritional insights with health recommendations. By combining multiple models with Redis for fast data retrieval, the system delivers an efficient and practical solution for promoting healthier food choices.
</p>
</div>

<div class="section box">
<h2>👩‍💻 Author</h2>
<p>
<b>Charishma Doki</b><br>
AI & ML Intern
</p>
</div>

</body>
</html>
