import streamlit as st
from utils.process_data import compare_prices

st.title("Food Price Comparator 🍔🍕")

food_name = st.text_input("Enter Food Name", "")
restaurant_name = st.text_input("Enter Restaurant Name", "")
city = st.text_input("Enter City", "")

if st.button("Compare Prices"):
    if food_name and restaurant_name and city:
        result = compare_prices(food_name, restaurant_name, city)
        st.success(result)
    else:
        st.warning("Please enter all details.")
        
# run ---> streamlit run app.py        