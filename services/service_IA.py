import streamlit as st
from openai import OpenAI

@st.cache_data(show_spinner=False)
def resumen_estadistico(estadisticas):
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        
        system_prompt = """
            Eres un analista estadístico profesional.
            Convierte resultados numéricos en conclusiones claras y ejecutivas.
            Explica qué significan los valores observados.
            Detecta y menciona posibles anomalías.
            Relaciona números con histogramas y boxplots.
            No recalcules estadísticas.
            No inventes datos.
            Sé breve, claro y útil.
            Máximo 170 palabras.
            """
        
        prompt_final = f"""Interpreta el siguiente resumen estadístico de la variable "{estadisticas['columna']}":
            Tamaño de muestra: {estadisticas['n']}
            Media: {estadisticas['media']}
            Desviación estándar: {estadisticas['std']}
            Mínimo: {estadisticas['min']}
            Máximo: {estadisticas['max']}
            IQR: {estadisticas['iqr']}
            Sesgo: {estadisticas['sesgo']}
            Normalidad: {estadisticas['normalidad']}
            Genera un reporte ejecutivo explicando qué significan estos resultados y qué mostrarían el histograma y boxplot."""
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=200,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_final}
            ],
            temperature=0.4
        )
        return response.choices[0].message.content
    except Exception as e:
        return None
    
def interpretar_prueba(estadisticas):
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        prompt_final = f"""
            Se realizó una prueba Z para la variable "{estadisticas['columna']}".
            Tamaño de muestra: {estadisticas['n']}
            Media muestral: {estadisticas['media']}
            Desviación estándar usada: {estadisticas['std']}
            Valor Z obtenido: {estadisticas['z']}
            p-value: {estadisticas['p_value']}
            Nivel de significancia alpha: {estadisticas['alpha']}
            Media hipotética: {estadisticas['mu_hipotetica']}
            Tipo de prueba: {estadisticas['tipo_prueba']}
            Decisión automática: {estadisticas['decision']}
            Explica qué significa este resultado, si existe evidencia estadística suficiente y si los supuestos de la prueba parecen razonables.
        """

        system_prompt = """
            Eres un consultor experto en inferencia estadística.
            Analiza resultados ya calculados de una prueba Z.
            No expliques teoría general innecesaria.
            Concéntrate en interpretar ESTE caso específico.
            Explica pruebas de hipótesis de forma clara para estudiantes.
            No recalcules valores.
            No inventes datos.
            Habla en lenguaje sencillo y profesional.
            Explica:
            - significado del valor Z
            - interpretación del p-value
            - decisión estadística
            - conclusión práctica
            - validez de supuestos
            Máximo 220 palabras.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=250,
            temperature=0.4,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_final}
            ]
        )

        return response.choices[0].message.content

    except Exception:
        return "No fue posible interpretar la prueba en este momento."