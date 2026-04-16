import pandas as pd
import numpy as np

def generar_datos(n_filas=100):
    np.random.seed(42)
    
    # 1. Distribución Normal (Edad)
    edades = np.random.normal(loc=35, scale=12, size=n_filas).astype(int)
    edades = np.clip(edades, 18, 90)
    
    # 2. Distribución Exponencial (Gasto Mensual)
    gastos = np.random.exponential(scale=500, size=n_filas)
    
    # 3. Distribución de Poisson (Número de Visitas al sitio)
    visitas = np.random.poisson(lam=8, size=n_filas)
    
    # 4. Distribución Binomial / Bernoulli (Suscripción Premium)
    es_premium = np.random.binomial(n=1, p=0.3, size=n_filas)
    
    # 5. Distribución Uniforme (Calificación de satisfacción)
    satisfaccion = np.random.uniform(1, 5, size=n_filas)

    df = pd.DataFrame({
        "ID_Cliente": range(1, n_filas + 1),
        "Edad": edades,
        "Gasto_USD": np.round(gastos, 2),
        "Visitas_Mes": visitas,
        "Premium": es_premium,
        "Satisfaccion": np.round(satisfaccion, 1)
    })
    
    return df