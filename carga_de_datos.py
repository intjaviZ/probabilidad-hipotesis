import streamlit as st
import pandas as pd
from services.clasificador_variables import detectar_variables

def main():
    st.set_page_config(page_title="App Estadística", layout="wide")

    st.title("DISTRIBUCIONES DE PROBABILIDAD Y PRUEBA DE HIPÓTESIS")
    st.header("Carga de datasets")

    file = st.file_uploader(label="Set de datos", type=["csv", "xlsx"], help="Carga un archivo CSV o Excel para comenzar el análisis",)
    
    if file is not None:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        
        st.session_state["data"] = df
        st.divider()
        
        st.dataframe(st.session_state["data"].head(n=30),  use_container_width=True)
        st.session_state["variables"] = detectar_variables(df)
        st.divider()
        
        numericas = st.session_state["variables"]["numericas"]
        if len(numericas) == 0:
            st.warning("No hay columnas numéricas para analizar")
        else:
            col1, col2 = st.columns(2)
            with col1:
                with st.container():
                    st.subheader("Numericas")
                    for i, d in enumerate(st.session_state['variables']['numericas'], start=1):
                        st.markdown(f"{i}. **{d}**")
            with col2:
                with st.container():
                    st.subheader("Candidatas continuas")
                    for i, d in enumerate(st.session_state['variables']['candidatas_continuas'], start=1):
                        st.markdown(f"{i}. **{d}**")
        
main()