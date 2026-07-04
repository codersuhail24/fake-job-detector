# 🕵️ Fake Job Posting Detector

A Machine Learning web application that detects whether a job posting is **Fake** or **Genuine** using Natural Language Processing (NLP) and XGBoost.

## 🚀 Features

- Detects fake job postings
- NLP-based text preprocessing
- TF-IDF Vectorization
- XGBoost Classifier
- Interactive Streamlit Web App
- Model persistence using Joblib

## 📊 Dataset

- Source: Kaggle Fake Job Postings Dataset
- Total Records: 17,880
- Fake Jobs: 866
- Genuine Jobs: 17,014

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib
- NLTK

## 📂 Project Structure

```
fake-job-detector/
│
├── data/
├── Fakejobdetector.ipynb
├── app.py
├── fake_job_detector.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
```

## ▶️ Run Locally

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

## 📈 Model

- TF-IDF Vectorizer
- XGBoost Classifier
- Accuracy: ~98%

## 👨‍💻 Author

Suhail Ahamed