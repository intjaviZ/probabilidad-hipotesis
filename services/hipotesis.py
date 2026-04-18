import numpy as np
from math import erf, sqrt


def normal_cdf(x):
    return (1 + erf(x / sqrt(2))) / 2


def z_test(data, mu0, alpha, test_type):
    n = len(data)
    mean = np.mean(data)
    sigma = np.std(data, ddof=1)
    se = sigma / np.sqrt(n)

    z = (mean - mu0) / se

    # p-value según tipo de prueba
    if test_type == "Bilateral":
        p_value = 2 * (1 - normal_cdf(abs(z)))

    elif test_type == "Cola izquierda":
        p_value = normal_cdf(z)

    else:  # Cola derecha
        p_value = 1 - normal_cdf(z)

    decision = "Se rechaza H0" if p_value < alpha else "No se rechaza H0"

    return {
        "z": z,
        "p_value": p_value,
        "decision": decision,
        "mean": mean,
        "sigma": sigma,
        "n": n
    }