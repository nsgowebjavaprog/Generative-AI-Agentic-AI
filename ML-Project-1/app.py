# project DATA SCIENCE

import streamlit as st
import pandas as pd 
import numpy as np 

## Title of Application

st.title("Hello Streamlit Application..!")

## Display Simple Text
st.write("This is a Simple Text")

## Create a Simple Data Frame

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column':[10,20,30,40]
})

# Display DataFrame

st.write("Here is the dataframe")
st.write(df)

##Create Line Chart

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)