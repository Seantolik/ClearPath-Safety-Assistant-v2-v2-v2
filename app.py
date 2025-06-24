
import streamlit as st
import openai
from prompts import PROMPTS, DESCRIPTIONS

# --- Page configuration ---
st.set_page_config(page_title="ClearPath Safety Assistant v2")

# --- Title ---
st.title("ClearPath Safety Assistant")

# --- Load API key ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Handle mode from query parameter ---
query_params = st.query_params
mode = query_params.get("mode", "assist")  # Default to assist

# Set initial prompt and description
system_prompt = PROMPTS.get(mode, PROMPTS["assist"])
description = DESCRIPTIONS.get(mode, DESCRIPTIONS["assist"])

# Display current mode description
st.markdown(f"**{description}**")

# --- Optional toggle shown only in consultant mode ---
if mode == "consultant":
    role = st.radio(
        "Choose your role:",
        ["Assist Mode", "Consultant Mode"],
        index=1,
        help="Switch between simplified guidance or expert-level risk management support."
    )
    if role == "Assist Mode":
        mode = "assist"
        system_prompt = PROMPTS["assist"]
        description = DESCRIPTIONS["assist"]
        st.markdown(f"**{description}**")

# --- Chat input ---
user_input = st.text_input("Enter your safety or compliance question:")
if user_input:
    with st.spinner("Generating response..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        st.write(response["choices"][0]["message"]["content"])
