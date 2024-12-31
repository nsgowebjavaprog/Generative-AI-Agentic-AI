import requests
import streamlit as st

def get_translation_response(input_text, target_language):
    json_body = {
        "input": {
            "text": "Hello",
            "language": "French"
        },
        "config": {},
        "kwargs": {}
    }
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()

# Streamlit app
st.title("LLM Translation Application")

# Input fields
input_text = st.text_input("Enter the text you want to translate")
target_language = st.selectbox("Select the target language", ["French", "Spanish", "German"])

# Button to trigger translation
if st.button("Translate"):
    if input_text and target_language:
        try:
            response = get_translation_response(input_text, target_language)
            st.write(response)
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter the text and select a target language.")
