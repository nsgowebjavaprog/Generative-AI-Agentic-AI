# Input & Display Output Project

import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")


age = st.slider("Select Your Age: ", 0, 100, 25)

st.write(f"Your Age is: {age}.")


option = ["Python", "JavaScript", "Java", "C++"]
choice = st.selectbox("Choose your Best one: ", option)
st.write(f"Your Best/favarate is: {choice}.")


if name:
    st.write(f"Hello, {name}")
    
data = {
    "Name" : ["NS LONI", "NS ", "LONI"],
    "Age": [20,19,18],
    "City": ["Indian", "Karnataka", "Bijapur"]
}

df = pd.DataFrame(data)
df.to_csv("simpledata.csv")
st.write(df)
    
# Upload Button

uploaded_file = st.file_uploader("Choose a CSV File", type="csv") 

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Display 
    st.write(df)  
    
    
# Run--------> streamlit run widgets.py