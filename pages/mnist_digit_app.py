import streamlit as st
import numpy as np
from tensorflow import load_model
from PIL import Image, ImageOps

st.set_page_config(page_title="MNIST Digit Classifier", layout="centered")

st.title("🧠 MNIST Digit Classifier")
st.write("Upload a handwritten digit image (28x28 grayscale) to classify it.")

# Load model
@st.cache_resource
def load_cnn_model():
    model = load_model("mnist_model.h5")
    return model

model = load_cnn_model()

# Upload image
uploaded_file = st.file_uploader("📤 Upload a digit image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    image = ImageOps.invert(image)                  # MNIST digits are white on black
    image = image.resize((28, 28))
    st.image(image, caption="Processed Image", width=150)

    img_array = np.array(image).astype("float32") / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(img_array)
    predicted_label = np.argmax(prediction)

    st.success(f"✅ Predicted Digit: **{predicted_label}**")
    st.bar_chart(prediction[0])