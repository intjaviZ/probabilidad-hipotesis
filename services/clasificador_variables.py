import pandas as pd

def detectar_variables(df):
    variables = {
        "numericas": [],
        "candidatas_continuas": [],
    }
    if df is None: return variables
    
    local_df = df.copy()    
    for col in local_df.columns:
        if pd.api.types.is_numeric_dtype(local_df[col]):
            variables['numericas'].append(col)
            if local_df[col].nunique() / len(local_df[col]) > 0.1:
                variables['candidatas_continuas'].append(col)
    return variables