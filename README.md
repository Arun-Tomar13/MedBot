# MedBot - AI-Powered Healthcare Chatbot 🚀

## 🏥 Overview
MedBot is an **AI-powered healthcare chatbot** designed to provide **preliminary medical guidance and assistance**. It utilizes **natural language processing (NLP)** techniques to analyze user input and generate appropriate responses. The chatbot integrates a **pre-trained GPT-2 model** along with a **rule-based healthcare keyword system** to enhance user experience.

---

## ✨ Features
✅ Provides **quick medical guidance** based on AI-generated responses and keywords.  
✅ Suggests **doctor appointments and emergency actions** when necessary.  
✅ Uses a **GPT-2 model** for intelligent conversational responses.  
✅ **Streamlit-based** web interface for easy accessibility.  
✅ Supports **NLTK** for text preprocessing (tokenization, stopword removal).  

---

## 📌 Tech Stack
- **Frontend**: Streamlit 🎨
- **Backend**: Python 🐍
- **Machine Learning**: Transformers (GPT-2) 🤖
- **Libraries Used**:
  - `streamlit` - Web UI framework
  - `transformers` - AI model processing
  - `nltk` - Text preprocessing
  - `torch` - Deep learning model execution

---

## 📸 Preview
### MedBot in Action:
![MedBot Preview1](https://github.com/Arun-Tomar13/Medbot_Intern/blob/main/img%201.png?raw=true)
![MedBot Preview2](https://github.com/Arun-Tomar13/Medbot_Intern/blob/main/img%202.png?raw=true)

---

## 🚀 Installation Guide
### 🛠 Prerequisites
Ensure you have **Python 3.8+** installed.

### 🔧 Setup Steps
#### 1️⃣ Clone the Repository
```sh
git clone <repository-url>
cd MedBot
```

#### 2️⃣ Create a Virtual Environment
##### Using `venv` (Recommended)
```sh
python -m venv venv
```

##### Using `virtualenv` (Alternative)
```sh
virtualenv venv
```

#### 3️⃣ Activate the Virtual Environment
##### On Windows (Command Prompt)
```sh
venv\Scripts\activate
```
##### On Windows (PowerShell)
```sh
venv\Scripts\Activate.ps1
```
##### On macOS/Linux
```sh
source venv/bin/activate
```

#### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

#### 5️⃣ Run the Application
```sh
streamlit run app.py
```

---

## 🛠 How It Works
1️⃣ User enters a **medical query** in the chat interface.  
2️⃣ The chatbot checks for **predefined healthcare keywords** to provide instant guidance.  
3️⃣ If no keyword matches, the **GPT-2 model** generates a contextual response.  
4️⃣ The **response is displayed** in the chat UI.  

---

## 📁 Project Structure
```
MedBot/
│── app.py                 # Main Streamlit application
│── requirements.txt       # List of dependencies
│── README.md              # Project documentation
```

---

## 🔮 Future Enhancements
🚀 Integration with **advanced medical databases**.  
🌍 Support for **multi-language processing**.  
☁️ Deployment as a **web service**.  

---

## ⚠️ Disclaimer
**MedBot is not a replacement for professional medical advice.** Always consult a healthcare provider for medical concerns.

---

## 📜 License
This project is open-source and available under the **MIT License**.
