import streamlit as st
import numpy as np
from cauer import Cauer
import plotly.graph_objs as go

st.title("🧮 Calculadora del Seno Elíptico")

st.latex(r'''Sn_{k}(z) =  \omega  \iff  \int_{0}^\omega \frac{d\omega}{\sqrt{1-\omega^2} \cdot \sqrt{1-k^2\omega^2}}  = z''')

z_str = st.text_input("Número complejo z", "1+0.5j")
k = st.number_input("Parámetro k", value=0.80, min_value=0.00, max_value=1.00, step=0.001, format="%0.3f")
fig = go.Figure()

try:
    cauer = Cauer()
    z_str =z_str.replace(" ", "")
    z = complex(z_str)
    sn = cauer.SenoEliptico(z=z, k=k)
    L = cauer.L_SN(k)
    Li = cauer.Li_SN(k)

    zeros = [{"re": 2*n*L, "im": 0} for n in range(-10, 10)]
    poles = [{"re": 2*n*L, "im": Li} for n in range(-10, 10)]

    fig.update_layout(
        xaxis_title="Real",
        yaxis_title="Imaginary",
        width=400, height=300,
        showlegend=False,
        xaxis=dict(title="Real", range=[-2.8*L, 2.8*L]),
        yaxis=dict(title="Imaginary", range=[-Li/10, 2*Li]),
    )
    fig.update_layout(
        shapes=[
            dict(
                type="line",
                x0=0, x1=0,
                y0=-Li/10, y1=2*Li,  # Match your y-axis range
                line=dict(color="#31333f", width=1)
            )
        ]
    )
    fig.add_trace(go.Scatter(
        x=[z.real],
        y=[z.imag],
        mode="markers",
        marker=dict(symbol="circle", size=12, color="green"),
        name="point"
    ))
    fig.add_trace(go.Scatter(
        x=[z["re"] for z in zeros],
        y=[z["im"] for z in zeros],
        mode="markers",
        marker=dict(symbol="circle", size=12, color="lightblue"),
        name="zeros"
    ))
    fig.add_trace(go.Scatter(
        x=[p["re"] for p in poles],
        y=[p["im"] for p in poles],
        mode="markers",
        marker=dict(symbol="x", size=14, color="red", line_width=2),
        name="poles"
    ))
    
    fig.update_layout(
        margin=dict(l=10, r=10, t=5, b=10)
    )



    st.plotly_chart(fig, use_container_width=True)
    st.success(f"$Sn_{{k}}(z) =  {np.real_if_close(sn):.4f}$")
    st.info(f"$L(k) =  {L:.4f}$")
    st.info(f"$L_i(k) = {Li:.4f}$")
except:
    st.error("Entrada inválida")