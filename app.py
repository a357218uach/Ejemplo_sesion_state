import streamlit as st
st.tittle("Ejemplo para usar session_state")

count = 0

increment = st.button("increment")
if increment:
  count += 1

st.write("Count =", count)
