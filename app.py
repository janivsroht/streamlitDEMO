import streamlit as st
st.title("CHRIST University")
st.header("Department of Computer Science")
st.subheader("Advanceed Python Programming")
st.write("Welcome to out Streamlit application")
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Welcome, ", name)
st.success("Application loaded successfully!!")