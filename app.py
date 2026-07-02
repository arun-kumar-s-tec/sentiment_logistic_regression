import streamlit as st
import pickle

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Social Media Sentiment Analyzer",
    page_icon="😊",
    layout="wide"
)

# -----------------------------
# Load Saved Files
# -----------------------------
with open("logistic_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

with open("label_encoder.pkl", "rb") as file:
    label_encoder = pickle.load(file)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

.big-font{
    font-size:40px !important;
    font-weight:bold;
    color:#4CAF50;
    text-align:center;
}

.small-font{
    font-size:18px;
    text-align:center;
    color:gray;
}

.result{
    padding:20px;
    border-radius:10px;
    font-size:25px;
    text-align:center;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<p class='big-font'>📊 Social Media Sentiment Analysis</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='small-font'>Logistic Regression + CountVectorizer + Streamlit</p>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("About")

st.sidebar.info(
"""
This application predicts the sentiment of social media text using a
Logistic Regression model.

Model:
- Logistic Regression

Vectorizer:
- CountVectorizer

Developed using:
- Python
- Scikit-Learn
- Streamlit
"""
)

# -----------------------------
# Input
# -----------------------------
user_input = st.text_area(
    "✍️ Enter your text",
    height=180,
    placeholder="Type your text here..."
)

# -----------------------------
# Predict
# -----------------------------
if st.button("🔍 Analyze Sentiment", use_container_width=True):

    if user_input.strip() == "":

        st.warning("Please enter some text.")

    else:

        vector = vectorizer.transform([user_input])

        prediction = model.predict(vector)

        sentiment = label_encoder.inverse_transform(prediction)[0]

        if sentiment.lower() == "positive":

            st.success(f"😊 Predicted Sentiment : {sentiment}")

        elif sentiment.lower() == "negative":

            st.error(f"😞 Predicted Sentiment : {sentiment}")

        else:

            st.info(f"😐 Predicted Sentiment : {sentiment}")

# -----------------------------
# Sample Inputs
# -----------------------------
st.divider()

st.subheader("💡 Try These Examples")

col1, col2, col3 = st.columns(3)

with col1:
    st.success(
        "I absolutely love this product. Amazing quality!"
    )

with col2:
    st.error(
        "Worst experience ever. Very disappointed."
    )

with col3:
    st.info(
        "The event was okay. Nothing special."
    )

st.divider()

st.caption("Made with ❤️ using Streamlit")