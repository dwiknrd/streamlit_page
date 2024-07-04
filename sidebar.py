import streamlit as st

st.title("Ini teks di halaman utama")

# Menampilkan teks di sidebar
with st.sidebar:
    st.header("Sidebar Header")
    st.text("Ini adalah teks di sidebar.")
    st.button("Tombol di sidebar")

