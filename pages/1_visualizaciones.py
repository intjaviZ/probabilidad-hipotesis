import streamlit as st
from plots.histograma import crear_histograma_kde
from  plots.bloxplot import crear_boxplot
from services.resumen_estadistico import resumen_estadistico
from services.interpretacion import analizar_distribucion

st.title("Visualización de distribuciones")

if "data" not in st.session_state:
    st.warning("Primero carga un dataset en la sección de carga de datos.")
    st.stop()
    
if "data" in st.session_state and st.session_state['variables']['candidatas_continuas']:
    df = st.session_state["data"]
    opciones = st.session_state['variables']['candidatas_continuas']
    
    variable_seleccionada = st.sidebar.selectbox("Variable candidata", opciones)
    bin_histograma = st.sidebar.slider("bin del histograma",min_value=1, max_value=10, value=2)
    if variable_seleccionada:
        serie = df[variable_seleccionada]
        resumen = resumen_estadistico(serie)
        
        st.subheader("Resumen estadístico")
        col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col1:
            st.metric("N", resumen["n"])
        with col2:
            st.metric("Desv. Est.", round(resumen["desv"], 2))

        with col3:
            st.metric("Media", round(resumen["media"], 2))
        with col4:
            st.metric("Mediana", round(resumen["mediana"], 2))
        with col5:
            st.metric("Mínimo", round(resumen["minimo"], 2))
        with col6:
            st.metric("Máximo", round(resumen["maximo"], 2))
        
        st.divider()
        st.subheader("Histograma")
        fig = crear_histograma_kde(serie, variable_seleccionada, bin_histograma)
        st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        st.subheader("Bloxplot")
        fig_box = crear_boxplot(serie, variable_seleccionada)
        st.plotly_chart(fig_box, use_container_width=True)
        
        
        resultado = analizar_distribucion(serie)
        st.divider()
        st.subheader("Interpretación automática")
        st.write(f"**¿La distribución parece normal?** {resultado['normalidad']}")
        st.write(f"**¿Hay sesgo?** {resultado['sesgo']}")
        st.write(f"**¿Hay outliers?** {resultado['outliers']}")
        
        st.subheader("Panel educativo")

        st.info("""
        **Histograma:** muestra cómo se distribuyen los datos según su frecuencia.  
        **Boxplot:** resume la dispersión de los datos, la mediana y posibles valores atípicos.  
        **Normalidad:** es importante porque muchas pruebas estadísticas paramétricas la consideran como supuesto.
        """)

else:
    st.warning("Por favor, carga los datos primero en la página principal.")