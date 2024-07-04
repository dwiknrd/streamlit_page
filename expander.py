import streamlit as st

# Menggunakan expander untuk menyembunyikan teks
with st.expander("Klik untuk melihat detail"):
    st.text("Ini adalah detail yang dapat di-expand.")
    st.text("Anda dapat menyembunyikan atau menampilkan kembali ini.")