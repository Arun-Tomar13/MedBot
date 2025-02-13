import streamlit as st
st.set_page_config(page_title="MedBot", layout="wide")

from streamlit_chat import message  
from transformers import AutoModelForCausalLM, AutoTokenizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import torch
import time



# Initialize session state for model loading
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False

@st.cache_resource(show_spinner=False)
def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)

# Initialize NLTK
download_nltk_data()

@st.cache_resource(show_spinner=False)
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_name = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    ).to(device)
    # Set pad token id in the model config
    model.config.pad_token_id = model.config.eos_token_id
    return model, tokenizer, device

# Load the model and tokenizer once
@st.cache_resource(show_spinner=False)
def initialize_chat_components():
    model, tokenizer, device = load_model()
    st.session_state.model_loaded = True
    return model, tokenizer, device

model, tokenizer, device = initialize_chat_components()


if st.session_state.model_loaded:
    try:
        loading_message.empty()
    except:
        pass

# Healthcare keywords dictionary for faster lookup
HEALTHCARE_RESPONSES = {
    "symptom": "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice.",
    "appointment": "Would you like me to schedule an appointment with a doctor?",
    "medication": "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor.",
    "pain": "If you're experiencing pain, it's important to understand its severity and duration. Please consult a healthcare provider.",
    "emergency": "If this is a medical emergency, please call emergency services immediately.",
    "fever": "If you have a fever, monitor your temperature and seek medical attention if it persists.",
    "doctor": "Would you like information about finding a doctor or scheduling an appointment?",
}

def healthcare_chatbot(user_input):
    try:
        user_input_lower = user_input.lower()
        for keyword, response in HEALTHCARE_RESPONSES.items():
            if keyword in user_input_lower:
                return response
        
        # Generate response with the model
        inputs = tokenizer(
            user_input,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
            add_special_tokens=True
        ).to(device)
        
        with torch.no_grad():
            outputs = model.generate(
                inputs.input_ids,
                max_length=100,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=0.7,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
        return response.strip()

    except Exception as e:
        return f"I apologize, but I encountered an error. Please try again. Error: {str(e)}"


def main():

    st.markdown("""
    <style>
    body { background-color:rgb(159, 91, 226); } /* Soft violet background */
    .stApp { background: linear-gradient(to right, #4b0082, #1e3a8a, #8b008b); }
    
    .header {
        font-size: 28px;
        font-weight: bold;
        color: #5E60CE;
        text-align: center;
    }

    .chat-container {
        width:80%;
        background-color: #ffffff;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin: 10px auto;
    }

    .user-msg {
        background-color: #FFC8DD;
        color: #5E60CE;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
    }

    .ai-msg {
        background-color: #A0C4FF;
        color: #1B4965;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
    }

    .loading-text {
        color: #9D4EDD;
        font-style: italic;
    }

    </style>
""", unsafe_allow_html=True)

#  Display Header
st.markdown('<p class="header">🩺 MedBot</p>', unsafe_allow_html=True)

#  Display Model Status
with st.spinner("⏳ Initializing your MedBot... Please wait."):
    time.sleep(2)
st.success("✅ your doctor(MedBot) Ready!")

#  Chat Interface
st.subheader("Chat with your personal Doctor 🤖")
st.write("💬 Type your medical question below:")

user_input = st.text_input("Your Message:", key="user_input")
if st.button("Ask"):
    if user_input:
        st.markdown(f'<div class="chat-container user-msg">👤 {user_input}</div>', unsafe_allow_html=True)

        # Simulating AI response delay
        with st.spinner("🤖 Thinking..."):
            time.sleep(2)
            ai_response = healthcare_chatbot(user_input)
        
        st.markdown(f'<div class="chat-container ai-msg">🩺 {ai_response}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
