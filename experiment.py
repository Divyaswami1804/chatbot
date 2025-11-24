import streamlit as st

with st.chat_message("assistant", "user", "ai","human"):
    st.audio_input("path/to/audio/file.mp")
    st.camera_input("take the picture")
    st.text_input("enter your name :")



