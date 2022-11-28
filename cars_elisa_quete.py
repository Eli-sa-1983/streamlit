import streamlit as st
import requests 
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.sidebar.header('CARS')
st.title('Vrouuuuum!! Vrouuummmm!!')


def accueil():
    
    st.sidebar.markdown('Cars')
    st.write(df_cars)

    
    

def page2():
    st.markdown("USA")
    st.sidebar.markdown("Oncle Sam")
   

def page3():
    st.markdown("Japan")
    st.sidebar.markdown("Soleil Levant")
    
def page4():
    st.markdown("Europe")
    st.sidebar.markdown("Vieux Continent")

page_names_to_funcs = {
    "Accueil": accueil,
    "USA": page2,
    "Japan": page3,
    "Europe": page4,
    }

selected_page = st.sidebar.selectbox("Chosissez votre page :", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


