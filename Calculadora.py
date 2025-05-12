import streamlit as st
import numpy as np
from cauer import Cauer

st.markdown("""
        <style>
               .block-container {
                    padding-top: 3rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.title("Calculadora del Seno Elíptico 🧮")

st.latex(r'''Sn_{k}(z) =  \omega  \iff  \int_{0}^\omega \frac{d\omega}{\sqrt{1-\omega^2} \cdot \sqrt{1-k^2\omega^2}}  = z''')

z_str = st.text_input("Argumento complejo z", "1+0.5j")
k = st.number_input("Parámetro k", value=0.80, min_value=0.00, max_value=1.00, step=0.001, format="%0.3f")


cauer = Cauer()

try:
    z_str =z_str.replace(" ", "")
    z = complex(z_str)
    sn = cauer.SenoEliptico(z=z, k=k)
    L = cauer.L_SN(k)
    Li = cauer.Li_SN(k)

    fig = cauer.config_figure(z, L, Li)

    st.success(f"$Sn_{{k}}(z) =  {np.real_if_close(sn):.4f}$")
    st.info(f"$L(k) =  {L:.4f}$")
    st.info(f"$L_i(k) = {Li:.4f}$")
    st.plotly_chart(fig, use_container_width=True)
except:
    st.error("Entrada inválida")