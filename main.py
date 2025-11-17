import streamlit as st

home = st.Page("home.py", title="Home", icon="🏠", default=True,)
profile = st.Page("pages/profile.py", title="Profile", icon="❄️")
meal_plan = st.Page("pages/meal plan.py", title="meal plan", icon="🎉")
feedback = st.Page("pages/chatbot.py", title="chatbot", icon="📄")

# Create a navigation bar
pg = st.navigation([home, profile, meal_plan, feedback])


# Run the selected page
pg.run()