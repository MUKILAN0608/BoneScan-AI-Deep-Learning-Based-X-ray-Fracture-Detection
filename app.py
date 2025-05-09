import streamlit as st
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
import os
import tensorflow as tf
from PIL import Image  # Needed for grayscale conversion

# Load the pre-trained model
model = load_model('bone_fracture_model.keras')

# Function to preprocess the image and make a prediction
def predict_image(img):
    # Convert to grayscale
    img = img.convert('L')  # 'L' mode for grayscale

    # Resize image to match the model's input shape
    img = img.resize((224, 224))

    # Convert the image to an array
    img_array = np.array(img)

    # Normalize the image
    img_array = img_array / 255.0

    # Add batch and channel dimensions (for grayscale images)
    img_array = np.expand_dims(img_array, axis=(0, -1))  # Shape: (1, 224, 224, 1)

    # Make a prediction
    prediction = model.predict(img_array)

    # Return the result
    if prediction[0][0] < 0.5:
        return "No Fracture"
    else:
        return "Fracture"

# Title of the app
st.title("Bone Fracture Detection App")

# Instructions
st.write("Upload an image of an X-ray for bone fracture detection:")

# Upload the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image using PIL
    img = Image.open(uploaded_file)

    # Display the image
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Make prediction when button is pressed
    if st.button('Predict'):
        prediction = predict_image(img)
        st.write(f"Prediction: {prediction}")
