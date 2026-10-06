import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Load trained model
with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)


# -------------------- CLEAR FUNCTION --------------------

def clear_all():
    st.session_state.cp = 0
    st.session_state.ca = 0
    st.session_state.thal = 3
    st.session_state.oldpeak = 0.0
    st.session_state.prediction = None


# -------------------- CUSTOM UI --------------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #f1f5f9;
}

[data-testid="stHeader"] {
    background-color: transparent;
}

/* Header */
.title {
    background: linear-gradient(135deg, #0f766e, #14b8a6);
    padding: 30px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

/* Patient information box */
.card {
    background-color: #0f766e;
    padding: 25px;
    border-radius: 15px;
    color: white;
    margin-bottom: 20px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-weight: bold;
    background-color: #0f766e;
    color: white;
    border: none;
}

.stButton > button:hover {
    background-color: #14b8a6;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# -------------------- HEADER --------------------

st.markdown("""
<div class="title">
    <h1>❤️ Heart Disease Prediction</h1>
    <p>Machine Learning Based Health Prediction System</p>
</div>
""", unsafe_allow_html=True)


# -------------------- PATIENT INFORMATION --------------------

st.markdown("""
<div class="card">
    <h3>Patient Information</h3>
    <p>Enter the following information to get a prediction.</p>
</div>
""", unsafe_allow_html=True)


# -------------------- INPUT FIELDS --------------------

if "cp" not in st.session_state:
    st.session_state.cp = 0

if "ca" not in st.session_state:
    st.session_state.ca = 0

if "thal" not in st.session_state:
    st.session_state.thal = 3

if "oldpeak" not in st.session_state:
    st.session_state.oldpeak = 0.0

if "prediction" not in st.session_state:
    st.session_state.prediction = None


cp = st.number_input(
    "Chest Pain Type (cp)",
    min_value=0,
    max_value=3,
    step=1,
    key="cp"
)

ca = st.number_input(
    "Major Vessels (ca)",
    min_value=0,
    max_value=3,
    step=1,
    key="ca"
)

thal = st.number_input(
    "Thalassemia (thal)",
    min_value=0,
    max_value=7,
    step=1,
    key="thal"
)

oldpeak = st.number_input(
    "ST Depression (oldpeak)",
    min_value=0.0,
    max_value=10.0,
    step=0.1,
    key="oldpeak"
)


st.write("")


# -------------------- BUTTONS --------------------

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Predict", use_container_width=True):

        patient_data = pd.DataFrame(
            [[cp, ca, thal, oldpeak]],
            columns=["cp", "ca", "thal", "oldpeak"]
        )

        prediction = model.predict(patient_data)

        st.session_state.prediction = prediction[0]


with col2:
    st.button(
        "🗑️ Clear All",
        use_container_width=True,
        on_click=clear_all
    )


# -------------------- RESULT --------------------

if st.session_state.prediction is not None:

    if st.session_state.prediction == 1:
        st.error("⚠️ Prediction: Heart Disease")
    else:
        st.success("✅ Prediction: No Heart Disease")


# -------------------- FOOTER --------------------

st.caption(
    "For educational purposes only. This system is not a medical diagnosis."
)
