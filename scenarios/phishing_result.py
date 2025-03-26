import streamlit as st

def show_phishing_result():
    st.title("Phishing Simulation Result")
    st.subheader(st.session_state.result_message)

