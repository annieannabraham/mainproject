from flask import Flask, render_template, request
import cv2
import numpy as np
import tensorflow as tf

# Load the deep learning model
model_save = tf.keras.models.load_model('model_save.h5')


# Create a Flask application
pra="panaromic_analyser"
app = Flask(pra)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for the prediction page
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['image']

    # Read the image file
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Preprocess the image
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Make a prediction with the model
    pred = model_save.predict(img)

    # Decode the prediction
    age = np.argmax(pred[0][:101])
    gender = np.argmax(pred[0][101:])

    # Return the predicted age and gender as a JSON response
    return {'age': str(age), 'gender': 'Male' if gender == 0 else 'Female'}
# Start the Flask application
if pra == 'pra':
    app.run(debug=True)

