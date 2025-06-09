import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Resume & Portfolio", layout="centered")

# Profile Section
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("profile.jpg")
    st.image(image, width=120)
with col2:
    st.title("👤 Mojtaba Roohi")
    st.write("💻 Aspiring Machine Learning Engineer")
    st.write("📧 Email: m.roohi916@gmail.com")
    st.write("🌐 GitHub: [github.com/mojtaba72075](https://github.com/mojtaba72075)")

st.markdown("---")

# Education
st.header("🎓 Education")
st.write("""
**B.Sc. in Chemical Engineering**  
Petroleum University of Technology, 2015  
GPA: 16.07 / 20
""")

# Work Experience
st.header("💼 Work Experience")
st.write("""
**Senior Chemist **, NISOC  
_Jul 2019 – Present  
- Built  classification models and regression models  
- Used pandas, scikit-learn, and matplotlib, tensor flow, keras
""")

# Projects / Portfolio
st.header("📁 Portfolio Projects")

with st.expander("🧠 MNIST Digit Classifier"):
    st.write("A CNN-based handwritten digit classifier built using TensorFlow and Streamlit.")
    st.write("✅ Users can upload an image of a digit and get prediction results.")
    st.page_link("pages/mnist_digit_app.py", label="🔍 Open App", icon="🔗")

# Optional: Theme Toggle
st.markdown("---")
st.write("© 2025 Mojtaba Roohi")