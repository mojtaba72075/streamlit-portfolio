import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Resume", layout="wide")

st.title("🧑‍💻 Mojtaba Roohi Resume & ML Portfolio")

# Sidebar Theme Toggle
theme = st.sidebar.radio("Select Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown(
        """
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
        """, unsafe_allow_html=True
    )

# Profile section
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("profile.jpg")
    st.image(image, width=120)
with col2:
    st.title("👤 Mojtaba Roohi")
    st.write("💻 Senior Chemist Interested in Machine Learning ")
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
**Senior Chemist**, NISOC  
_Jul 2019 – Present
           
**Process Engineer**, Persian Gulf Bidboland Gas Refining Company\n 
_Oct 2018 – Jul 2019
           
**Process Engineer**, Aria Phosphoric Jonoub\n 
_May 2018 – Oct 2018 
         
**Engineer of Production Management**, NISOC\n 
_Jan 2016 – Oct 2017  
                                        
- Built  classification and regression models  
- Used pandas, scikit-learn, matplotlib, tensor flow, keras
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