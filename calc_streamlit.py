import streamlit as st
import numpy as np
import scipy.special
import scipyx as scx



class Cauer:
    def __init__(self, k= None):
        self.k = k

    def SenoEliptico(self, z, k):
        sn, cn, dn, ph = scx.ellipj(u=z, m=k**2)
        return sn

    def L_SN(self, k):
        return float(np.real(scipy.special.ellipk(k**2)))

    def Li_SN(self, k):
        return float(scipy.special.ellipk(1 - k**2))
    

st.title("🧮 Calculadora del Seno Elíptico")

z_str = st.text_input("Número complejo z", "0.5+0.5j")
k = st.number_input("Parámetro k", value=0.8, min_value=0.0, max_value=1.0, step=0.01)

try:
    cauer = Cauer()
    z_str =z_str.replace(" ", "")
    z = complex(z_str)
    sn = cauer.SenoEliptico(z=z, k=k)
    L = cauer.L_SN(k)
    Li = cauer.Li_SN(k)

    st.success(f"Sn(z, k): {np.real_if_close(sn):.4f}")
    st.info(f"L(k): {L:.4f}")
    st.info(f"Li(k): {Li:.4f}")
except:
    st.error("Entrada inválida")