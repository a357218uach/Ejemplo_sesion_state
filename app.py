import streamlit as st
st.title ("Ejemplo para usar session_state")

if "key" not in st.session_state:
  st.session_state["key"] = "valor"
  
count = 0

increment = st.button("increment")
if increment:
  count += 1

st.write("Count =", count)
