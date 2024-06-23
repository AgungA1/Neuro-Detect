import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow import keras
from description.glioma import app as glioma
from description.meningioma import app as meningioma
from description.pituitary import app as pituitary

def app():
    model = keras.models.load_model('Web/vgg16.h5')

    labels = open('web/labels.txt').read().split('\n')
    st.write("# Scanner")

    uploaded_file = st.file_uploader("Choose an image...")
    if uploaded_file is not None:
        image = tf.io.decode_image(uploaded_file.getvalue(), channels=3, dtype=tf.float32)
        image = tf.image.resize(image, [128, 128])
        image = tf.expand_dims(image, axis=0)
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width="auto")

        prediction = model.predict(image)
        predicted_class = labels[np.argmax(prediction)]
        st.write(f"Prediction: {predicted_class}")
        st.write(f"Confidence: {np.max(prediction*100, axis=1)[0]:.2f}%")

        if predicted_class == "glioma":
            glioma()
        elif predicted_class == "meningioma":
            meningioma()
        elif predicted_class == "pituitary":
            pituitary()
        else:
            st.warning("Tidak Terdeteksi Tumor.")