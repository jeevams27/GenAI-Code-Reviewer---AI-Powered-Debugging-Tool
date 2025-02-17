import streamlit as st
import google.generativeai as ai

# Configure API Key
ai.configure(api_key="my api key")

# Enhanced System Prompt
sys_prompt = """
You are an expert AI Python code reviewer. 
Your role is to help students and developers by analyzing Python code, identifying errors, and providing solutions.
Always provide detailed explanations, including the root cause of errors and best practices for improvement.

**Guidelines:**
1. If the code has errors, identify and explain them under a section titled **"Bug Report"**.
2. Provide an improved version of the code under a section titled **"Corrected Code"**.
3. If the user asks about a non-Python topic, politely decline and ask them to provide Python-related queries.
4. Always include an encouragement message at the end:  
   *"If you need more help, refer to the official Python documentation: [Python Docs](https://docs.python.org/3/)"*

Your responses should always maintain a helpful, professional, and constructive tone.
"""

# Initialize Gemini Model
gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit UI
st.title("🔍 AI Python Code Reviewer")

user_input = st.text_area(label="Enter your Python Code", placeholder="Paste your code here...")

btn_click = st.button("Debug!")

if btn_click:
    if user_input.strip():
        response = gemini_model.generate_content(user_input)
        st.write(response.text)
    else:
        st.warning("Please enter Python code before clicking 'Debug!'.")