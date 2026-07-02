# 📊 Social Media Sentiment Analysis using Logistic Regression

A Machine Learning web application built using **Logistic Regression**, **CountVectorizer**, and **Streamlit** to classify social media text into sentiment categories.

---

## 🚀 Project Overview

This project predicts the sentiment of social media posts using Natural Language Processing (NLP) techniques and Logistic Regression.

The application accepts user-entered text, converts it into numerical features using CountVectorizer, and predicts whether the sentiment is Positive, Negative, or Neutral.

---
Working Link : Click Here()

## ✨ Features

- 📂 Load and preprocess social media sentiment dataset
- 🧹 Data cleaning and preprocessing
- 🔤 Text feature extraction using CountVectorizer
- 🤖 Logistic Regression model training
- ⚙️ Hyperparameter tuning using GridSearchCV
- 📊 Model evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - Confusion Matrix
- 💾 Save trained model using Pickle
- 🌐 Interactive Streamlit Web Application
- ✍️ Real-time sentiment prediction

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- CountVectorizer
- Logistic Regression
- Matplotlib
- Seaborn
- Streamlit
- Pickle

---

## 📁 Project Structure

```
Social-Media-Sentiment-Analysis/
│
├── app.py
├── logistic_model.pkl
├── vectorizer.pkl
├── label_encoder.pkl
├── Social_Media_Sentiment.csv
├── requirements.txt
├── README.md
└── Sentiment_Analysis.ipynb
```

---

## 📊 Machine Learning Workflow

```
Dataset
    │
    ▼
Data Cleaning
    │
    ▼
Duplicate & Missing Value Handling
    │
    ▼
Label Encoding
    │
    ▼
CountVectorizer
    │
    ▼
Train-Test Split
    │
    ▼
Logistic Regression
    │
    ▼
Hyperparameter Tuning
    │
    ▼
Model Evaluation
    │
    ▼
Save Model
    │
    ▼
Streamlit Deployment
```

---

## 📈 Model Evaluation

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Classification Report
- Confusion Matrix

Hyperparameter tuning was performed using **GridSearchCV** to obtain the best Logistic Regression model.

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/social-media-sentiment-analysis.git
```

Move into the project directory

```bash
cd social-media-sentiment-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💡 Example Inputs

### Positive

```
I absolutely love this product. Amazing quality!
```

### Negative

```
Worst experience ever. Completely disappointed.
```

### Neutral

```
The event was okay. Nothing special.
```

---

## 📸 Application Preview

You can add screenshots here after deployment.

```
Home Screen

Prediction Result

Example Inputs
```

---

## 📌 Future Improvements

- TF-IDF Vectorizer comparison
- Support Vector Machine implementation
- Random Forest comparison
- Deep Learning model
- Sentiment confidence score
- Model explainability
- Deployment using Streamlit Cloud

---

## 👨‍💻 Author

**Akshay Kumar S**

Medical Mechatronics Student

Machine Learning | Python | Data Science | Full Stack Development

---

## ⭐ If you found this project useful, consider giving it a Star!
