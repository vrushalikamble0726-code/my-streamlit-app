
import streamlit as st

# Application Title
st.title("Simple Streamlit App")

# Add a text input
name = st.text_input("Enter your name")

# Display the entered text
if name:
    st.success("Hello, " + name)

# Welcome message
st.write("Welcome to my Machine Learning Application!")
