##  🥑 Personalized AI Nutrition Chatbot

This project is a multi-page Streamlit application that provides highly personalized and safe daily nutrition and meal recommendations. It uses the Google Gemini API, specifically the gemini-2.5-flash-preview-09-2025 model, to generate recommendations based on structured user data (age, weight, goals, and allergies).

The application focuses on safety and personalization by passing the user's profile information directly to the LLM via a powerful System Instruction.

### 🚀 Features

Profile Management: Save your age, weight, dietary purpose (Weight Loss, Muscle Gain, etc.), and strict allergies in a dedicated Profile page (profile.py).

Personalized Recommendations: The Chatbot page (pages/chatbot.py) uses your saved profile data to inform every recommendation.

Safety-First Design: The LLM is strictly instructed to exclude all specified allergens from the meal plans.

Structured Output: Recommendations include daily meal structure, estimated nutritional breakdown, restrictions to avoid, and meal prep tips.

### 🛠️ Setup and Installation

#### Prerequisites

* Python 3.8+

* A Google Gemini API Key

* Local Installation

* Clone the repository (or extract the files):

git clone [your-repo-link]
cd "final project"


#### Create a virtual environment (Recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:

The required packages are listed in requirements.txt.
pip install -r requirements.txt

Set up the API Key:
Create a file named .env in the root of the project directory (final project/) and add your API key. Do not use quotes. e.g GOOGLE_API_KEY=AIzaSy...your...key...here...XYZ

Running the App
Run the main application file using Streamlit:

streamlit run main.py
(main.py is your main entry point, as suggested by the multi-page structure.)

The app will open in your browser at http://localhost:8501.
also check out the app here at "https://final-project-sdg2-2.streamlit.app/"

### 📂 Project Structure

final project/ 

├── .env                  
├── home.py               
├── nav.py                
├── requirements.txt      
├── README.md            
└── pages/
    ├── chatbot.py        
    ├── profile.py        
    └── meal plan.py      
