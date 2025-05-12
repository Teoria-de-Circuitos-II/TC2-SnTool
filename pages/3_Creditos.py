import streamlit as st

st.set_page_config(
    page_title="Créditos",
    page_icon="✍️",
)
st.title('Créditos ✍️')

st.markdown('La integral elíptica fue descubierta por Niels Henrik Abel:')

left_pad, center_col, right_pad = st.columns([1, 3, 1])
with center_col:
    # Niels Henrik Abel section
   
    st.image('Niels_Henrik_Abel.jpg', width=300)  # Fixed width of 300px
    
    # Wilhelm Cauer section

st.markdown('La función aproximación de mínimo orden fue definida por Wilhelm Cauer:')
left_pad, center_col, right_pad = st.columns([1, 3, 1])
with center_col:

    st.image('photo_cauer.jpg', width=300)  # Same fixed width for consistency
    
# Credits section
st.markdown('La siguiente aplicación fue realizada por la cátedra Teoría de Circuitos 2 del ITBA:')
st.markdown("- Candela Gioia")
st.markdown("- Juan Francisco Sbruzzi")
st.markdown("- Javier Petrucci")