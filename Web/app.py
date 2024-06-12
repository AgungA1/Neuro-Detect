import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('vgg16-tya.h5')

labels = open('labels.txt').read().split('\n')
st.write("# NeuroDetect")

uploaded_file = st.file_uploader("Choose an image...")
if uploaded_file is not None:
    image = tf.io.decode_image(uploaded_file.getvalue(), channels=3, dtype=tf.float32)
    image = tf.image.resize(image, [128, 128])
    image = tf.expand_dims(image, axis=0)
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    prediction = model.predict(image)
    predicted_class = labels[np.argmax(prediction)]
    st.write(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {np.max(prediction*100, axis=1)[0]:.2f}%")
