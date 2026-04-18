import plotly.figure_factory as ff
import plotly.graph_objects as go

def crear_histograma_kde(serie, nombre_variable, custom_bin):
    fig = ff.create_distplot(
        [serie.dropna().values],
        [nombre_variable],
        show_hist=True,
        show_rug=False,
        curve_type='kde',
        bin_size=custom_bin
    )            
    fig.update_traces(
        marker=dict(line=dict(width=1, color='white')), # Bordes blancos suelen verse más limpios
        selector=dict(type='histogram')
    )
    fig.update_layout(
        title=dict(
            text=f"Análisis de Distribución: {nombre_variable}",
            x=0.5,
            xanchor='center'
        ),
        xaxis_title=nombre_variable,
        yaxis_title="Densidad de Probabilidad",
        template="plotly_white",
        height=500,
        showlegend=False, # Como es una sola variable, la leyenda a veces sobra
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig