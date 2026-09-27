
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

api_key = os.getenv("Groq_key")

# Check API key
if not api_key:
    st.error("Groq_key not found in .env file")
    st.stop()

# Create Groq client
client = Groq(api_key=api_key)

# Page Settings

st.set_page_config(
    page_title="Generative AI App",
    page_icon="🤖"
)

# Title

st.title("🤖 Generative AI Application")

st.write("Text generation using Groq LLM")

# Prompt Type

prompt_type = st.selectbox(
    "Choose Prompt Type",
    [
        "Simple Explanation",
        "Summary",
        "Generate Ideas",
        "Write Code"
    ]
)

# User Prompt

user_prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: Explain Artificial Intelligence"
)

# Generate Button

if st.button("🚀 Generate"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:
        
        if prompt_type == "Simple Explanation":

            final_prompt = f"""
            Explain {user_prompt}
            in very simple words.
            Give one easy example.
            """

        elif prompt_type == "Summary":

            final_prompt = f"""
            Give a short and clear summary
            about the following topic:

            {user_prompt}
            """

        elif prompt_type == "Generate Ideas":

            final_prompt = f"""
            Generate 5 creative ideas
            about:

            {user_prompt}
            """

        elif prompt_type == "Write Code":
            final_prompt = f"""
            Write beginner-friendly Python code
            for:
            {user_prompt}
            Explain the code clearly.
            """
        try:
            with st.spinner("Generating response..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful AI assistant."
                        },
                        {
                            "role": "user",
                            "content": final_prompt
                        }
                    ]
                )
            st.subheader("🤖 AI Response")
            st.write(
                response.choices[0].message.content
            )
        except Exception as e:

            st.error(f"Error: {e}")