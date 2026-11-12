import streamlit as st

st.set_page_config(
    page_title="MARGEN - Asistente de Lectura",
    page_icon="📚",
    layout="wide"
)

st.title("📚 MARGEN: Tu Compañero Inteligente de Lectura")
st.markdown("""
Bienvenido a **MARGEN**, un sistema interactivo diseñado para enriquecer tus sesiones de lectura, 
fusionando el control ambiental, el seguimiento de hábitos literarios y la gestión de notas personales.
""")

st.info("👈 Utiliza el menú lateral izquierdo para navegar entre los diferentes ambientes y herramientas de la aplicación.")

st.subheader("💡 ¿Qué encontrarás en esta aplicación?")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌌 Mi Universo de Lectura")
    st.write("Controla tus sesiones activas, simula el cambio de ambientación lumínica/sonora y realiza un seguimiento visual de tus métricas de lectura.")

with col2:
    st.markdown("### 🛋️ Mi Espacio de Lectura")
    st.write("Un entorno enfocado en la reflexión personal, el registro de fragmentos destacados y la construcción de memoria de tus libros.")
