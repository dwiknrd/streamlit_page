import streamlit as st

# Menampilkan konten dalam tab-tab
tabs = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

# Konten Tab 1
with tabs[0]:
    st.header("Konten Tab 1")
    st.text("Ini adalah konten dari Tab 1.")

# Konten Tab 2
with tabs[1]:
    st.header("Konten Tab 2")
    st.text("Ini adalah konten dari Tab 2.")

# Konten Tab 3
with tabs[2]:
    st.header("Konten Tab 3")
    st.text("Ini adalah konten dari Tab 3.")