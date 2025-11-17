import streamlit as st
from datetime import datetime

st.markdown("# home ❄️")
st.sidebar.markdown("# home❄️")
st.set_page_config(page_title="NutriMind AI", page_icon="🧠", layout="wide")


st.title("Welcome to NutriMind AI 🥗")
st.subheader("Eat Smart, Live Better with AI-Powered Nutrition",divider='red')


 

st.markdown("""
    ### Why Choose NutriMind AI?
    #### Our intelligent system learns about you and creates meal plans that fit your unique lifestyle
    """)




col1, col2, col3 = st.columns(3)

with col1:
    st.write('')  # Empty line for spacing
    st.markdown("""
    <div style="background-color: #ffffff; color: #00008B; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #00a8e8;">
    <h4>🤖 AI-Powered Plans</h4>
    <p>Get personalized meal recommendations powered by advanced AI technology</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.write('')  # Empty line for spacing
    st.markdown("""
    <div style="background-color: #ffffff; color: #00008B; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #9d4edd;">
    <h4>🎯 Goal-Focused</h4>
    <p>Whether it's weight loss, muscle gain, or maintenance - we've got you covered</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.write('')  # Empty line for spacing
    st.markdown("""
    <div style="background-color:#ffffff; color: #00008B; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #52b788;">
    <h4>💚 Health First</h4>
    <p>Balanced nutrition that considers your allergies and preferences</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div style="background-color: #ffffff; color: #00008B; padding: 25px; border-radius: 10px; text-align: center; margin: 20px 0; border: 2px solid #ff9800;">
<h3>Ready to Transform Your Nutrition?</h3>
<p>Join thousands of users who are already experiencing the benefits of AI-powered meal planning. Start your personalized journey today!</p>
</div>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Start Your Journey"):
        st.switch_page("pages/profile.py")

