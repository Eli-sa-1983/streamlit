import streamlit as st
import requests 
from PIL import Image

st.image('logo-grenoble.png',width=600)

st.sidebar.header('Les Dott!')


def accueil():
    
    st.sidebar.markdown('Les Dott de Grenoble!')
    st.title('Dott, Trottinettes et Velos de Grenoble!')
    st.image('logo-grenoble.png')
    

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Accueil": accueil,
    "Page 2": page2,
    "Page 3": page3,
    }

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.sidebar.image('dott_gre.jpeg',width=300)

