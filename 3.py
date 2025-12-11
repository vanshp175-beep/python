
import streamlit as st
st.title("welcome to streamlit")
username=st.text_input("Enter username")
password=st.text_input("Enter password")
if st. button("Login"):
    if username=="admin":
        if password=="1234":
            st.success("Valid user")
        else:
            st.error("Invalid pasword")
    else:
        st.error("Invalid username")
        
