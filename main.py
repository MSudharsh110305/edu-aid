import stre amlit as st
from modules.ai_response import get_ai_response

# Initialize Streamlit app
st.title("EduAid - AI-Powered Educational Assistant")

# Prompt input
st.subheader("Enter a prompt for AI assistance:")
user_prompt = st.text_input("Prompt")

# Get AI Response
if st.button("Get AI Response") and user_prompt:
    response = get_ai_response(user_prompt)
    st.write("AI Response:")
    st.write(response)
