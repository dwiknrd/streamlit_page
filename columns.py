import streamlit as st

# Memisahkan layar menjadi 2 kolom
col1, col2 = st.columns(2)

# Menampilkan teks di kolom pertama
with col1:
    st.header("Kolom Pertama")
    st.text("Ini adalah teks di kolom pertama.")

# Menampilkan teks di kolom kedua
with col2:
    st.header("Kolom Kedua")
    st.text("Ini adalah teks di kolom kedua.")