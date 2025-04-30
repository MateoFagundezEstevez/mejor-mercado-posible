import streamlit as st
from openai import OpenAI, APIStatusError

st.title("¿Dónde puedo vender mi producto?")
st.write("Escribí qué producís y dónde, y te sugeriremos mercados potenciales.")

producto = st.text_input("¿Qué producís y en qué lugar?")

if st.button("Buscar mercado ideal") and producto:
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sos un asesor de comercio internacional que recomienda mercados para productos."},
                {"role": "user", "content": f"Produzco {producto}. ¿Dónde me conviene venderlo y por qué?"}
            ]
        )

        st.success(respuesta.choices[0].message.content)

    except APIStatusError as e:
        if "rate_limit" in str(e).lower():
            st.error("🚫 Superaste el límite de uso de tu cuenta OpenAI. Esperá un momento y volvé a intentarlo.")
        else:
            st.error(f"💥 Ocurrió un error con OpenAI: {str(e)}")

    except Exception as e:
        st.error(f"⚠️ Error inesperado: {str(e)}")
