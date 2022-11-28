import streamlit as st
import requests 
from PIL import Image


st.sidebar.header('CARS')


def accueil():
    
    st.sidebar.markdown('Cars')
    st.title('Cars')
    
    

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


