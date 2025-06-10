## --- FILE: core/session.py
import streamlit as st

def init_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'api_key' not in st.session_state:
        st.session_state.api_key = None
