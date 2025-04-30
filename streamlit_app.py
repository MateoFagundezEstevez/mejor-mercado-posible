import streamlit as st
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage

st.set_page_config(page_title="Asistente OpenAI", page_icon="🤖")
st.title("🤖 Tu Asistente AI con tu propia API Key")

st.markdown("Ingresá tu clave personal de OpenAI para usar esta app con tus propios tokens.")

user_api_key = st.text_input("🔑 Clave API", type="password")
model = st.selectbox("🧠 Modelo", ["gpt-3.5-turbo", "gpt-4"])
user_input = st.text_area("✍️ Tu pregunta", height=150)

if st.button("Enviar") and user_api_key and user_input:
    try:
        client = OpenAI(api_key=user_api_key)  # NUEVO ENFOQUE

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": user_input}]
        )

        st.success("✅ Respuesta:")
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"💥 Error: {e}")

