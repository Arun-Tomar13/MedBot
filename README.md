# MedBot - AI-Powered Healthcare Chatbot

## Overview
MedBot is an AI-powered healthcare chatbot designed to provide preliminary medical guidance and assistance. It uses natural language processing (NLP) techniques to analyze user input and generate appropriate responses. The chatbot integrates a pre-trained GPT-2 model and a rule-based healthcare keyword system to enhance user experience.

## Features
- Provides quick medical guidance based on keywords and AI-generated responses.
- Suggests doctor appointments and emergency actions when necessary.
- Utilizes a GPT-2 model for generating conversational responses.
- Streamlit-based web interface for easy accessibility.
- Supports natural language processing (NLTK) for tokenization and stopword removal.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Transformers (GPT-2)
- **Libraries Used**:
  - `streamlit` for web UI
  - `transformers` for AI model processing
  - `nltk` for text preprocessing
  - `torch` for deep learning model execution

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed.

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd MedBot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   streamlit run app.py
   ```

## How It Works
1. The user enters a medical query in the chat interface.
2. The chatbot first checks for predefined healthcare keywords to provide instant guidance.
3. If no keyword matches, the GPT-2 model generates a response based on context.
4. The response is displayed in the chat UI.

## File Structure
```
MedBot/
│── app.py                 # Main Streamlit application
│── requirements.txt       # List of dependencies
│── README.md              # Project documentation
```

## Future Enhancements
- Integration with more advanced medical databases.
- Support for multi-language processing.
- Deployment as a web service.

## Disclaimer
MedBot is not a replacement for professional medical advice. Always consult a healthcare provider for medical concerns.

## License
This project is open-source and available under the MIT License.

