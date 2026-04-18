def resumen_estadistico(serie):
    return {
        "n": serie.count(),
        "media": serie.mean(),
        "mediana": serie.median(),
        "desv": serie.std(),
        "minimo": serie.min(),
        "maximo": serie.max(),
    }