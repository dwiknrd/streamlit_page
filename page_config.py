import streamlit as st

# Konfigurasi halaman aplikasi
st.set_page_config(
    page_title="My Streamlit App",  # Judul halaman
    page_icon="🎈",                 # Icon halaman (Unicode emoji)
    layout="wide",                  # Layout halaman ("wide")
    initial_sidebar_state="expanded"  # Kondisi awal sidebar ("expanded")
)

# Konten aplikasi Streamlit
st.title("Hello, Streamlit!")
st.write("Welcome to my Streamlit app.")