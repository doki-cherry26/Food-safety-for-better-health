from flask import Flask, render_template, request
import numpy as np
import os
import json
import redis
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ---------------- REDIS CONNECTION ----------------
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


# ---------------- LOAD MODELS ----------------
cnn_model = load_model("C:\\Users\\chari\\Downloads\\projects\\redis\\models\\CNN_model .h5")
resnet_model = load_model("C:\\Users\\chari\\Downloads\\projects\\redis\\models\\resent.json.h5")
vgg_model = load_model("C:\\Users\\chari\\Downloads\\projects\\redis\\models\\vgg16_model.h5")


# ---------------- CLASS NAMES ----------------
class_names = [
    "apple_pie","baked_potato","burger","butter_naan","chai","chapathi",
    "cheesecake","chicken_curry","chole_bhature","crispy_chicken",
    "dal_makhani","dhokla","donut","fried_rice","french_fries","hot_dog",
    "ice_cream","idli","jalebi","kaathi_roll","kadai_paneer","kulfi",
    "masala_dosa","momos","omelette","pani_puri","pakode","pav_bhaji",
    "pizza","samosa","sandwich","sushi","taco","taquito"
]


# ---------------- HELPER: Normalize Keys ----------------
def normalize(text):
    return text.lower().replace(" ", "_")


# ---------------- PREDICT FUNCTION ----------------
def predict_image(img_path, model):

    img = image.load_img(img_path, target_size=model.input_shape[1:3])
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100

    return index, confidence


# ---------------- MAIN ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def index():

    image_path = None
    prediction = None
    confidence = None
    accuracy = None
    precision = None
    recall = None
    f1_score = None
    matrix = None
    nutrients = None
    selected_model = "CNN"

    if request.method == "POST":

        selected_model = request.form.get("model", "CNN")

        if "predict_btn" in request.form:

            file = request.files.get("file")

            if file and file.filename != "":
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)
                image_path = "/" + filepath

                # -------- MODEL SELECTION --------
                if selected_model == "CNN":
                    idx, confidence = predict_image(filepath, cnn_model)
                    matrix_key = "CNN_matrix"

                elif selected_model == "ResNet":
                    idx, confidence = predict_image(filepath, resnet_model)
                    matrix_key = "resnet_matrix"

                else:
                    idx, confidence = predict_image(filepath, vgg_model)
                    matrix_key = "vgg16_matrix"

                prediction = class_names[idx]
                normalized_prediction = normalize(prediction)

                # -------- FETCH METRICS FROM REDIS --------
                metrics_json = r.get(matrix_key)

                if metrics_json:
                    metrics = json.loads(metrics_json)

                    accuracy = round(metrics["test_accuracy"] * 100, 2)

                    report = metrics.get("classification_report", {})

                    # Find matching key safely
                    for key in report.keys():
                        if normalize(key) == normalized_prediction:
                            class_data = report[key]

                            precision = round(class_data["precision"] * 100, 2)
                            recall = round(class_data["recall"] * 100, 2)

                            # If f1 not stored, calculate
                            if precision + recall > 0:
                                f1_score = round(
                                    (2 * precision * recall) / (precision + recall),
                                    2
                                )
                            else:
                                f1_score = 0

                            matrix = class_data["confusion_matrix"]
                            break

                # -------- FETCH NUTRIENTS FROM REDIS --------
                nutrient_key = f"food:{normalized_prediction}"
                nutrients_json = r.get(nutrient_key)

                if nutrients_json:
                    nutrients = json.loads(nutrients_json)

    return render_template("index.html",
                           image_path=image_path,
                           prediction=prediction,
                           confidence=confidence,
                           accuracy=accuracy,
                           precision=precision,
                           recall=recall,
                           f1_score=f1_score,
                           matrix=matrix,
                           nutrients=nutrients,
                           class_names=class_names,
                           selected_model=selected_model)


if __name__ == "__main__":
    app.run(debug=True)