import streamlit as st
import os
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
# The following import is not strictly necessary for this file but is generally needed for the profile page
# from datetime import datetime 
# import pandas as pd 

# Load environment variables from .env file
load_dotenv() 

# --- Configuration ---
# Use the appropriate model for chat/text tasks
GEMINI_MODEL = "gemini-2.5-flash-preview-09-2025" 
API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Nutrition Chatbot", layout="centered")

st.markdown("# 🥑 Personalized Nutrition Chatbot")
st.sidebar.markdown("# 🥑 Nutrition Profile")

# Initialize session state for the chat history and profile if not present
if "messages" not in st.session_state:
    st.session_state.messages = []
if "profile" not in st.session_state:
    st.session_state["profile"] = {}

def format_profile_data(profile):
    """Formats the structured profile data into a clean string for the LLM prompt."""
    if not profile:
        return "No comprehensive profile data saved. Rely only on the user's latest query."
        
    allergies_str = ", ".join(profile.get("allergies", ["None"])) or "None"
    
    data_points = {
        "Age": f"{profile.get('age', 'N/A')} years",
        "Weight": f"{profile.get('weight_kg', 'N/A')} kg",
        "Dietary Purpose": profile.get('purpose', 'General health'),
        "Known Allergies": allergies_str
    }
    
    formatted_data = "\n".join([f"- {k}: {v}" for k, v in data_points.items()])
    return f"**User Profile Data:**\n{formatted_data}\n"

def get_nutrition_recommendations(user_query, profile_data_str):
    """
    Generate nutrition meal recommendations based on user query and saved profile.
    
    This function uses the robust Gemini 2.5 Flash model and includes the 
    user's structured data in the system instruction to ensure personalization.
    """
    if not API_KEY:
        return "Error: GOOGLE_API_KEY environment variable not set."

    # Use the structured profile data in the system instruction to anchor the response
    system_instruction = f"""You are a friendly, expert nutritional advisor. Your task is to provide personalized and safe meal recommendations.

    ALWAYS adhere to the following safety and personalization guidelines:
    {profile_data_str}
    
    Based on the profile above and the user's specific request below, provide a detailed, single response that covers the following four points:
    1. Recommended daily meal structure (e.g., breakfast, lunch, dinner, snack).
    2. Nutritional breakdown estimate (e.g., approximate calories, protein, carbs, fat).
    3. Dietary restrictions/allergies to strictly avoid (based on the profile).
    4. Two practical meal prep and cooking tips related to the recommendations.
    
    Format your response clearly using markdown headings and lists."""

    try:
        chat = ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=API_KEY,
            temperature=0.6 # Keep temperature moderate for structured recommendations
        )
        
        # The user's specific question or request is the HumanMessage content
        message = HumanMessage(content=user_query)
        
        response = chat.invoke(
            [message],
            config={"system_instruction": system_instruction}
        )
        
        return response.content

    except Exception as e:
        st.error(f"An API error occurred: {e}")
        return "Sorry, I couldn't generate recommendations right now. Please check the API key and try again."

# --- Main Chatbot Interface ---
# Format the saved profile data to be sent to the model
profile_data_for_prompt = format_profile_data(st.session_state.get("profile", {}))

# Display current profile status
st.sidebar.markdown("---")
if st.session_state.get("profile"):
    st.sidebar.success("✅ Profile Loaded")
    st.sidebar.markdown(profile_data_for_prompt)
else:
    st.sidebar.warning("⚠️ No comprehensive profile data saved. Please fill out your profile details on your profile page for personalized recommendations.")


user_input = st.chat_input("Ask for your personalized nutrition recommendations...")

if user_input:
    # 1. Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 2. Get recommendation using the profile data
    with st.spinner("Thinking... generating personalized nutrition plan..."):
        recommendation = get_nutrition_recommendations(user_input, profile_data_for_prompt)
    
    # 3. Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": recommendation})

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])