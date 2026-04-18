import streamlit as st
from services.resumen_estadistico import resumen_estadistico
from services.hipotesis import z_test
from services.guardar_estadisticas import guardar_estadisticas
from plots.hipotesis_plot import plot_z_curve

st.title("Prueba de hipótesis (Z)")

if "data" not in st.session_state:
    st.warning("Primero carga un dataset en la sección de carga de datos.")
    st.stop()
    
if "data" in st.session_state and st.session_state['variables']['candidatas_continuas']:
    df = st.session_state["data"]
    opciones = st.session_state['variables']['candidatas_continuas']
    
    variable_seleccionada = st.sidebar.selectbox("Variable candidata", opciones)
    data = df[variable_seleccionada].dropna()
    resumen = resumen_estadistico(data)
    mu0 = st.sidebar.number_input("Media hipotética (μ₀)", value=float(resumen["media"]), step=0.1)
    test_type = st.sidebar.radio("Tipo de prueba",options=["Bilateral", "Cola izquierda", "Cola derecha"])
    alpha = st.sidebar.selectbox("Nivel de significancia (α)", options=[0.10, 0.05, 0.01], index=1)
    
    st.subheader(f"Contexto de la variable seleccionada: {variable_seleccionada}")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Tamaño de muestra", resumen['n'])
    with col2:
        st.metric("Desv. estándar", f"{resumen['desv']:.2f}")
    with col3:
        st.metric("Media", f"{resumen['media']:.2f}")
    with col4:
        st.metric("Mínimo", f"{resumen['minimo']:.2f}")
    with col5:
        st.metric("Máximo", f"{resumen['maximo']:.2f}")
        
    st.divider()
    run_test = st.sidebar.button("Ejecutar prueba Z", use_container_width=True)
    if run_test:

        result = z_test(data, mu0, alpha, test_type)

        st.subheader("Resultados")

        r1, r2, r3 = st.columns(3)

        with r1:
            st.metric("Estadístico Z", f"{result['z']:.4f}")

        with r2:
            st.metric("p-value", f"{result['p_value']:.6f}")

        with r3:
            st.metric("Decisión", result["decision"])
        
        if test_type == "Bilateral":
                h1_text = "la media poblacional es diferente de μ₀"
        elif test_type == "Cola izquierda":
            h1_text = "la media poblacional es menor que μ₀"
        else:
            h1_text = "la media poblacional es mayor que μ₀"
        st.info(h1_text)
            
        st.divider()
        fig = plot_z_curve(result["z"], alpha, test_type)
        st.plotly_chart(fig, use_container_width=True)
        
        # Actualizar estado con todas las estadísticas
        st.session_state["estadisticas"] = guardar_estadisticas(
            col=variable_seleccionada,
            resumen=resumen,
            result=result,
            alpha=alpha,
            mu0=mu0,
            test_type=test_type
        )
        
        st.subheader("Interpretación y contexto")

        with st.container():    
            st.markdown(f"""
                ### Elementos clave

                - **Hipótesis nula (H₀):** la media poblacional es igual a μ₀  
                - **Hipótesis alternativa (H₁):** {h1_text}
                - **Nivel de significancia (α):** probabilidad de rechazar H₀ cuando es verdadera  
                - **p-value:** probabilidad de observar un resultado igual o más extremo que el obtenido  

                ---

                ### Regla de decisión

                - Si **p-value < α → Se rechaza H₀**
                - Si **p-value ≥ α → No se rechaza H₀**
                """
            )
            st.divider()
            st.info("En esta implementación se utiliza la **desviación estándar muestral** como aproximación de la desviación estándar poblacional (σ).")
else:
    st.warning("Por favor, carga los datos primero en la página principal.")