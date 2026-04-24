#  Emotion Detection System (Django + DeepFace)
 

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Framework-green?logo=django)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv)
![DeepFace](https://img.shields.io/badge/DeepFace-AI-orange)
![TextBlob](https://img.shields.io/badge/TextBlob-NLP-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

![GitHub repo size](https://img.shields.io/github/repo-size/fathiimmaa/sentimental-analysis)
![GitHub stars](https://img.shields.io/github/stars/fathiimmaa/sentimental-analysis?style=social)
![GitHub forks](https://img.shields.io/github/forks/fathiimmaa/sentimental-analysis?style=social)

A **multimodal emotion detection web application** built using Django that can analyze emotions from:

- 🎥 Live webcam feed  
- 📸 Uploaded images  
- 💬 Text input (sentiment analysis)

---

## 🚀 Features

- ✅ Real-time **face emotion detection** using webcam  
- ✅ **Image-based emotion detection**  
- ✅ **Text sentiment analysis** (Positive / Negative / Neutral)  
- ✅ Simple and clean **web interface (HTML + CSS)**  
- ✅ Built with Python and AI libraries  

---

## 🛠️ Technologies Used

- Python  
- Django  
- OpenCV  
- DeepFace  
- TextBlob  
- NumPy  
- HTML / CSS  

---

```
emotion_project/
│
├── emotion_project/ # Main project folder
│ ├── settings.py
│ ├── urls.py
│
├── detector/ # App folder
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ ├── index.html
│ │ ├── image.html
│ │ ├── text.html
│ ├── static/
│ │ └── style.css
│
├── manage.py
```
---

---

## ⚙️ Installation Guide

### 🔹 1. Clone the repository

```bash
git clone https://github.com/your-username/emotion-detection.git
cd emotion-detection
```
```
pip install -r requirements.txt
pip install django opencv-python deepface textblob numpy
python -m textblob.download_corpora
```

## 🎯 Usage

### 🎥 Live Emotion Detection
- Click **Live Detection**
- Webcam will open
- Emotion will be displayed on face

---

### 📸 Image Emotion Detection
- Go to **Image Upload**
- Upload an image
- Detected emotion will be shown

---

### 💬 Text Sentiment Analysis
- Enter a sentence
- Output will be:
  - Positive 😊
  - Negative 😞
  - Neutral 😐

---

## ⚠️ Notes

- Webcam must be enabled for live detection  
- First run of DeepFace may take time (model loading)  
- Ensure all dependencies are installed correctly  

---

## 🧠 Future Enhancements

- 📊 Emotion analytics dashboard  
- 🎤 Voice emotion detection  
- 🗄️ Save history to database  
- 📱 Mobile responsive UI  
- 🎨 Advanced UI with Bootstrap  

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📄 License

This project is for educational purposes.

## Author

Fathima




## 📁 Project Structure
