import numpy as np
import plotly.graph_objects as go
from math import erf, sqrt


def normal_pdf(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-(x ** 2) / 2)


def inverse_normal(p, tol=1e-5):
    low, high = -5, 5

    while high - low > tol:
        mid = (low + high) / 2
        cdf = (1 + erf(mid / sqrt(2))) / 2

        if cdf < p:
            low = mid
        else:
            high = mid

    return (low + high) / 2


def plot_z_curve(z, alpha, test_type):
    x = np.linspace(-4, 4, 800)
    y = normal_pdf(x)

    fig = go.Figure()

    # curva principal
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="lines",
        name="Normal estándar"
    ))

    # -------------------------
    # regiones críticas
    # -------------------------

    if test_type == "Bilateral":
        z_crit = inverse_normal(1 - alpha / 2)

        left_x = x[x <= -z_crit]
        right_x = x[x >= z_crit]

        fig.add_trace(go.Scatter(
            x=left_x,
            y=normal_pdf(left_x),
            fill="tozeroy",
            mode="none",
            name="Rechazo"
        ))

        fig.add_trace(go.Scatter(
            x=right_x,
            y=normal_pdf(right_x),
            fill="tozeroy",
            mode="none",
            name="Rechazo"
        ))

        title = "Prueba Bilateral"

    elif test_type == "Cola izquierda":
        z_crit = inverse_normal(alpha)

        left_x = x[x <= z_crit]

        fig.add_trace(go.Scatter(
            x=left_x,
            y=normal_pdf(left_x),
            fill="tozeroy",
            mode="none",
            name="Rechazo"
        ))

        title = "Prueba Cola Izquierda"

    else:
        z_crit = inverse_normal(1 - alpha)

        right_x = x[x >= z_crit]

        fig.add_trace(go.Scatter(
            x=right_x,
            y=normal_pdf(right_x),
            fill="tozeroy",
            mode="none",
            name="Rechazo"
        ))

        title = "Prueba Cola Derecha"

    # -------------------------
    # línea estadístico z
    # -------------------------

    fig.add_vline(
        x=z,
        line_dash="dash",
        annotation_text=f"Z = {z:.2f}",
        annotation_position="top"
    )

    fig.update_layout(
        title=title,
        xaxis_title="Z",
        yaxis_title="Densidad",
        template="plotly_white",
        height=500
    )

    return fig