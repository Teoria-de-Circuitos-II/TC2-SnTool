import streamlit as st

st.set_page_config(
    page_title="Créditos",
    page_icon= "✍️",
)
st.title('Créditos ✍️')

image_info_list = [{'text':'La integral elíptica fue descubierta por Niels Henrik Abel: ' , 'path': 'Niels_Henrik_Abel.jpg'}, {'text':  'La siguiente aplicación fue realizada por la cátedra Teoría de Circuitos 2 del ITBA:', 'path': 'photo_cauer.jpg'}]



grid = st.grid()
for image_info in image_info_list:
    row = grid.row()
    row.markdown()
    row.image(image_info.image)




st.markdown("- Candela Gioia")
st.markdown("- Juan Francisco Sbruzzi")
st.markdown("- Javier Petrucci")
            
