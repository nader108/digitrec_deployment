import tensorflow as tf
import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from PIL import Image
# load
Dig_model = tf.keras.models.load_model("C:/Users/PC/digitrec_deployment/dig_model.keras")


st.title("MNIST Digit Recognizer")
st.write("enter your photo")


uploaded_file = st.file_uploader("load img", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("L")
    st.image(image, caption="img", use_column_width=True)


    if st.button("Predict"):

        image_resized = image.resize((28, 28))
        image_array = np.array(image_resized) / 255.0
        image_array = image_array.reshape(1, 28, 28, 1)


        predictions = Dig_model.predict(image_array)
        predicted_digit = np.argmax(predictions)


        st.success(f"num is : {predicted_digit}")
        # st.write(f"احتمالات كل الأرقام: {predictions}")


