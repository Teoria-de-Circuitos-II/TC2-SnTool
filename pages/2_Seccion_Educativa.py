import streamlit as st

st.set_page_config(
    page_title="Educativo",
    page_icon="🧠",
)


st.title('Sección Educativa 🧠')


st.markdown('Se define la **integral elíptica incompleta de primera especie** en la forma algebraica de Jabobi como:')

st.latex(r'''F(\omega,k) =  \int_{0}^\omega \frac{d\omega}{\sqrt{1-\omega^2} \cdot \sqrt{1-k^2\omega^2}}''')

st.markdown(f'A partir de la integral anterior, se define el **seno elíptico de parámetro $k$** como: ')

st.latex(r'''Sn_{k}(z) =  \omega  \iff  \int_{0}^\omega \frac{d\omega}{\sqrt{1-\omega^2} \cdot \sqrt{1-k^2\omega^2}}  = z''')


st.markdown(f'El semi período **real** del seno elíptico de parámetro $k$ se denomina $L$ y se corresponde con la **integral elíptica completa de primera especie**, la cual se define de la siguiente manera: ')

st.latex(r''' L(k) =  \int_{0}^{1} \frac{d\omega}{\sqrt{1-\omega^2} \cdot \sqrt{1-k^2\omega^2}} ''')

st.markdown('La integral anterior se puede computar utilizando  la media geométrica aritmética como: ')

st.latex(r''' L(k) = \frac{\pi}{2\cdot AGM(1, \sqrt{1-k^2})}''')





st.markdown(f'El semi período **imaginario** del seno elíptico de parámetro $k$ se denomina $L_i$, el cual se calcula como: ')

st.latex(r'''  L_i(k) =  \int_{1}^{\frac{1}{k_1}} \frac{d\omega}{\sqrt{1-\omega^2} \cdot \sqrt{1-k^2\omega^2}} ''')


st.markdown('Existe una relación complementaria entre ambos semi períodos: ')

st.latex(r''' L_i(k) = L(\sqrt{1-k^2})''')

st.markdown('Por lo tanto, se puede computar el semi período imaginario como: ')

st.latex(r''' L_i(k) =\frac{\pi}{2\cdot AGM(1, k)}''')



st.markdown(f'El período real del seno elíptico es $4L$ y el período imaginario es $2L_i$. ')
st.markdown( 'Por lo tanto se cumple la propiedad fundamental de doble periocidad de las funciones elípticas: ')

st.latex(r'''Sn_{k}(z + 4L)  =  Sn_{k}(z)''')
st.latex(r'''Sn_{k}(z + j \cdot 2L_i)  =  Sn_{k}(z)''')


st.image('L_Li.png')

