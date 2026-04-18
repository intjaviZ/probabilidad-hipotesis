# plots/boxplot.py

import plotly.graph_objects as go


def crear_boxplot(serie, nombre_variable):
    fig = go.Figure()

    fig.add_trace(
        go.Box(
            x=serie.dropna(),
            name=nombre_variable,
            orientation="h",
            boxmean=True,
            marker=dict(size=6),
            line=dict(width=2)
        )
    )

    fig.update_layout(
        title=f"Boxplot de {nombre_variable}",
        xaxis_title=nombre_variable,
        template="plotly_white",
        height=350,
        showlegend=False
    )

    return fig