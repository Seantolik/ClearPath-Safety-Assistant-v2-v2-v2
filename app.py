
import streamlit as st
import openai
import os

# Page config
st.set_page_config(page_title="ClearPath Safety Assistant v2")

# Load logo
st.image("https://github.com/Seantolik/ClearPath-Safety-Assistant-v2-v2-v2/blob/main/Media/clearpath-logo-narrow.png", use_column_width=False)

# Load OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Get mode from query string
query_params = st.query_params
mode = query_params.get("mode", ["consultant"])[0]

# Define system prompts
PROMPTS = {
    "assist": "You are a trusted safety and risk management assistant. Your role is to explain complex safety and regulatory requirements in simple, helpful, and encouraging terms. You are an expert in environmental health and safety, construction, healthcare, social services, and transportation compliance. Focus on clarity, helpful next steps, and resources a small business or nonprofit could actually use.",
    "consultant": "You are a seasoned EHS and risk management consultant who supports commercial insurance producers. You specialize in property, casualty, and workers’ compensation risk analysis, loss prevention, and client compliance readiness. Provide technical guidance, OSHA standard interpretation, and strategic recommendations using accurate regulatory references and a confident, professional tone."
}

DESCRIPTIONS = {
    "assist": "Clear and helpful guidance for workplace injury prevention and compliance requirements.",
    "consultant": "Technical guidance for insurance producers and EHS consultants in mid-market commercial risk."
}

# Determine system prompt and description
system_prompt = PROMPTS.get(mode, PROMPTS["consultant"])
description = DESCRIPTIONS.get(mode, DESCRIPTIONS["consultant"])

# Optionally show mode toggle
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

st.markdown(f"### {description}")

# Main input
user_input = st.text_area("What’s your safety or compliance question?", height=150)

# Generate response
if st.button("Get Answers"):
    if user_input:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.3,
                max_tokens=1200
            )
            answer = response["choices"][0]["message"]["content"]
            st.markdown("#### Answer")
            st.write(answer)
    else:
        st.warning("Please enter a question first.")
