def analizar_distribucion(serie):
    serie = serie.dropna()

    # Métricas base
    media = serie.mean()
    mediana = serie.median()
    desv = serie.std()
    skew = serie.skew()

    # -----------------------------
    # Normalidad heurística
    # -----------------------------
    diferencia = abs(media - mediana)

    puntos = 0

    # media cercana a mediana
    if desv != 0 and diferencia <= (desv * 0.15):
        puntos += 1

    # skewness cercana a cero
    if -0.5 <= skew <= 0.5:
        puntos += 1

    # resultado textual
    if puntos == 2:
        normalidad = "Aproximadamente normal."
    elif puntos == 1:
        normalidad = "Moderadamente cercana a una distribución normal."
    else:
        normalidad = "No parece seguir una distribución normal."

    # -----------------------------
    # Sesgo
    # -----------------------------
    if -0.5 <= skew <= 0.5:
        sesgo = "Distribución bastante simétrica."
    elif 0.5 < skew <= 1:
        sesgo = "Ligero sesgo positivo (cola hacia la derecha)."
    elif skew > 1:
        sesgo = "Sesgo positivo marcado (cola hacia la derecha)."
    elif -1 <= skew < -0.5:
        sesgo = "Ligero sesgo negativo (cola hacia la izquierda)."
    else:
        sesgo = "Sesgo negativo marcado (cola hacia la izquierda)."

    # -----------------------------
    # Outliers con IQR
    # -----------------------------
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3 - q1

    limite_inf = q1 - 1.5 * iqr
    limite_sup = q3 + 1.5 * iqr

    outliers = serie[(serie < limite_inf) | (serie > limite_sup)]
    cantidad = len(outliers)

    if cantidad == 0:
        texto_outliers = "No se detectaron valores atípicos."
    elif cantidad <= 3:
        texto_outliers = f"Se detectaron pocos valores atípicos ({cantidad})."
    else:
        texto_outliers = f"Se detectaron varios valores atípicos ({cantidad})."

    return {
        "normalidad": normalidad,
        "sesgo": sesgo,
        "outliers": texto_outliers
    }