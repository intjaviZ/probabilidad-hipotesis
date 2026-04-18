import streamlit as st
from services.service_IA import resumen_estadistico, interpretar_prueba

st.title("Asistente IA")

if "data" in st.session_state and "estadisticas" in st.session_state:
    col1, col2 = st.columns(2)
    
    
    with col1:
        generar_resumen = st.button("Generar reporte", use_container_width=True)
    with col2:
        generar_interpretacion = st.button("Interptetar prueba", use_container_width=True)
        
    if generar_resumen: 
        with st.spinner("Analizando resultados..."):
            texto = resumen_estadistico(st.session_state["estadisticas"])
            st.write(texto)
        st.divider()
            
    if generar_interpretacion:
        with st.spinner("Analizando resultados..."):
            texto = interpretar_prueba(st.session_state["estadisticas"])
            st.write(texto)
else:
    st.warning("Por favor, carga los datos primero en la página principal.")