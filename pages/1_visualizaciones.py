import streamlit as st

st.title("📈 Visualización de distribuciones")

st.info("Aquí se mostrarán histogramas, KDE y boxplots.")

if "data" not in st.session_state:
    st.warning("Primero carga un dataset en la sección de carga de datos.")
    st.stop()