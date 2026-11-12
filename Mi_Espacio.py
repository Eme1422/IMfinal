import streamlit as st

st.title("🛋️ Mi Espacio de Lectura")
st.markdown("Registra tus reflexiones, anota fragmentos importantes y evalúa tus avances literarios.")

tab1, tab2 = st.tabs(["📝 Bitácora de Reflexiones", "📈 Progreso de Libros"])

with tab1:
    st.subheader("Registro de Notas y Opiniones")
    book_title = st.text_input("Título del libro actual:")
    user_thought = st.text_area("¿Qué te dejó este fragmento o capítulo?")
    
    if st.button("Guardar Reflexión"):
        if book_title and user_thought:
            st.success(f"Reflexión guardada exitosamente para: *{book_title}*")
            st.write(f"> \"{user_thought}\"")
        else:
            st.warning("Por favor completa el título y la reflexión antes de guardar.")

with tab2:
    st.subheader("Tu Huella de Lectura")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Libros leídos este mes", value="3")
    with col_b:
        st.metric(label="Páginas totales recorridas", value="482")
    
    st.progress(65, text="Meta de lectura anual (65% completado)")
