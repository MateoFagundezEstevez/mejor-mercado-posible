import streamlit as st
import openai

st.set_page_config(page_title="Asistente OpenAI Personal", page_icon="🧠")
st.title("🤖 Tu Asistente AI con tu propia API Key")

st.markdown("""
Ingresa tu clave personal de OpenAI para usar esta app con tus propios tokens.  
Podés generar una clave en [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys).
""")

# Ingreso seguro de API Key
user_api_key = st.text_input("🔑 Clave API de OpenAI", type="password", help="Tu clave no se almacena en ningún lado.")

# Selección de modelo
model = st.selectbox("🧠 Elegí el modelo a usar", ["gpt-3.5-turbo", "gpt-4"])

# Entrada del mensaje
user_input = st.text_area("✍️ Escribí tu mensaje o pregunta", height=150)

if st.button("Enviar") and user_api_key and user_input:
    openai.api_key = user_api_key

    with st.spinner("Pensando..."):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": user_input}]
            )
            st.success("✅ Respuesta del asistente:")
            st.write(response.choices[0].message.content)

        except openai.error.AuthenticationError:
            st.error("❌ Clave API inválida. Verificá e intentá de nuevo.")
        except openai.error.RateLimitError:
            st.error("⚠️ Límite de uso superado para esta clave.")
        except openai.error.InvalidRequestError as e:
            st.error(f"🚫 Solicitud inválida: {e}")
        except Exception as e:
            st.error(f"💥 Error inesperado: {e}")

elif st.button("Enviar"):
    st.warning("Por favor, ingresá tu clave API y una pregunta.")

