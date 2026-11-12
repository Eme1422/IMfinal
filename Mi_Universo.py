import streamlit as st

st.title("🌌 Mi Universo de Lectura")
st.markdown("Controla el estado de tu sesión de lectura actual y adapta el ambiente físico de la habitación de forma virtual.")

# Simulación de estados del dispositivo (Hardware emulado en software)
if "session_active" not in st.session_state:
    st.session_state.session_active = False

if "current_env" not in st.session_state:
    st.session_state.current_env = "Neutral"

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🕹️ Control de Sesión")
    if not st.session_state.session_active:
        if st.button("▶ Iniciar Sesión de Lectura", type="primary"):
            st.session_state.session_active = True
            st.success("¡Sesión iniciada! Disfruta tu lectura.")
            st.rerun()
    else:
        if st.button("⏹ Finalizar Sesión", type="secondary"):
            st.session_state.session_active = False
            st.warning("Sesión finalizada y guardada en el historial.")
            st.rerun()

with col2:
    st.subheader("📊 Estado del Dispositivo")
    if st.session_state.session_active:
        st.markdown("🟢 **Estado:** Lectura Activa")
        st.metric(label="Tiempo estimado de sesión", value="15 min")
    else:
        st.markdown("🔴 **Estado:** En Pausa / Reposo")
        st.metric(label="Tiempo estimado de sesión", value="0 min")

st.divider()

st.subheader("🎨 Selección de Ambiente Físico (Simulación de Luces)")
env_option = st.radio(
    "Elige la atmósfera para acompañar tu lectura:",
    ["Neutral", "☕ Café Literario", "🌧️ Lluvia Nocturna", "🌲 Bosque Profundo"],
    horizontal=True
)

if env_option != st.session_state.current_env:
    st.session_state.current_env = env_option
    st.toast(f"Ambiente cambiado a: {env_option}", icon="✨")

# Feedback visual según el ambiente elegido
if st.session_state.current_env == "☕ Café Literario":
    st.info("💡 Luz cálida ambiental y tonos ámbar simulados.")
elif st.session_state.current_env == "🌧️ Lluvia Nocturna":
    st.info("💧 Iluminación azulada tenue y sonido de fondo simulado.")
elif st.session_state.current_env == "🌲 Bosque Profundo":
    st.info("🌿 Tonos verdes suaves y atmósfera de concentración.")
else:
    st.info("⚪ Iluminación estándar de lectura.")
