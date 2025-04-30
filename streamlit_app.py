import streamlit as st
import openai

st.set_page_config(page_title="Asistente OpenAI", page_icon="🤖")
st.title("🤖 Tu Asistente AI con tu propia API Key")

st.markdown("Ingresa tu clave personal de OpenAI para usar esta app con tus propios tokens.")

# Entrada segura de API Key
user_api_key = st.text_input("🔑 Clave API", type="password")

# Selector de modelo
model = st.selectbox("🧠 Modelo", ["gpt-3.5-turbo", "gpt-4"])

# Entrada del usuario
user_input = st.text_area("✍️ Tu pregunta", height=150)

if st.button("Enviar") and user_api_key and user_input:
    try:
        openai.api_key = user_api_key

        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": user_input}]
        )

        st.success("✅ Respuesta:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        if "Incorrect API key" in str(e):
            st.error("❌ Clave API inválida.")
        elif "quota" in str(e).lower():
            st.error("⚠️ Superaste tu cuota de uso.")
        else:
            st.error(f"💥 Error inesperado: {e}")
elif st.button("Enviar"):
    st.warning("Ingresá tu clave y pregunta primero.")
