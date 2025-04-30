import streamlit as st
from openai import OpenAI

st.title("¿Dónde puedo vender mi producto?")
st.write("Escribí qué producís y dónde, y te sugeriremos mercados potenciales.")

producto = st.text_input("¿Qué producís y en qué lugar?")

if st.button("Buscar mercado ideal") and producto:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sos un asesor de comercio internacional que recomienda mercados para productos."},
            {"role": "user", "content": f"Produzco {producto}. ¿Dónde me conviene venderlo y por qué?"}
        ]
    )
    
    st.success(respuesta.choices[0].message.content)
