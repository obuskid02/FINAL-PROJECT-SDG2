import streamlit as st
from datetime import datetime
import pandas as pd
 
# Simple profile page form
st.title("User Profile")

if "profile" not in st.session_state:
    st.session_state["profile"] = {}

options = ["General health", "Weight loss", "Muscle gain", "Medical", "Other"]
current_purpose = st.session_state["profile"].get("purpose")
purpose_index = options.index(current_purpose) if current_purpose in options else 0

with st.form(key="profile_form"):
    age = st.number_input(
        "Age",
        min_value=0,
        max_value=130,
        value=int(st.session_state["profile"].get("age", 30)),
        step=1,
    )
    weight = st.number_input(
        "Weight (kg)",
        min_value=0.0,
        max_value=500.0,
        value=float(st.session_state["profile"].get("weight", 70.0)),
        format="%.1f",
    )
    allergies = st.text_area(
        "Allergies (comma-separated)",
        value=st.session_state["profile"].get("allergies", ""),
    )
    purpose = st.selectbox("Purpose", options=options, index=purpose_index)
    submitted = st.form_submit_button("Save profile")

if submitted:
    profile = {
        "age": int(age),
        "weight_kg": float(weight),
        "allergies": [a.strip() for a in allergies.split(",")] if allergies.strip() else [],
        "purpose": purpose,
        "updated_at": datetime.now().isoformat(),
    }
    st.session_state["profile"] = profile
    st.success("Profile saved")

# Display current profile if available
if st.session_state.get("profile"):
    p = st.session_state["profile"]
    st.subheader("Current profile")
    df = pd.DataFrame(
        {
            "field": ["age", "weight_kg", "allergies", "purpose", "updated_at"],
            "value": [
                p.get("age"),
                p.get("weight_kg"),
                ", ".join(p.get("allergies", [])),
                p.get("purpose"),
                p.get("updated_at"),
            ],
        }
    ).set_index("field")
    st.table(df)