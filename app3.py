import streamlit as st

st.title("🌐 Application de Test")

name = st.text_input("Quel est votre prénom ?")

if name:
    st.success(f"Bonjour {name} ! Bienvenue sur l'app de test 😊")

st.write("Ceci est une application de démonstration faite avec Streamlit.")
