import streamlit as st

def guardar_estadisticas(col, resumen, result,alpha, mu0, test_type):
    serie = st.session_state["data"][col].dropna()

    # Cuartiles
    q1 = serie.quantile(0.25)
    q2 = serie.quantile(0.50)
    q3 = serie.quantile(0.75)

    # Rango intercuartílico
    iqr = q3 - q1

    # Sesgo
    sesgo = serie.skew()

    # Clasificación simple de normalidad basada en sesgo
    if abs(sesgo) < 0.5:
        normalidad = "Aproximadamente normal"
    elif abs(sesgo) < 1:
        normalidad = "Ligero sesgo"
    else:
        normalidad = "Sesgo considerable"
        
    return {
        "columna": col,
        "n": resumen["n"],
        "media": resumen["media"],
        "std": resumen["desv"],
        "min": resumen["minimo"],
        "max": resumen["maximo"],
        "q1": round(q1, 4),
        "q2": round(q2, 4),
        "q3": round(q3, 4),
        "iqr": round(iqr, 4),
        "sesgo": round(sesgo, 4),
        "normalidad": normalidad,
        "z": result["z"],
        "p_value": result["p_value"],
        "decision": result["decision"],
        "alpha": alpha,
        "mu_hipotetica": mu0,
        "tipo_prueba": test_type,
    }