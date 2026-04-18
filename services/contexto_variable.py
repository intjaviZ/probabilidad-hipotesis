def contexto_variable(data):
    return {
        "n": len(data),
        "mean": data.mean(),
        "std": data.std(ddof=1),
        "min_val": data.min(),
        "max_val": data.max(),
    }