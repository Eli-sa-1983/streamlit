
import streamlit as st
import requests 
import pandas as pd
import seaborn as sns
import matplotlib as plt
from PIL import Image



st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars





option_velo = st.sidebar.selectbox(
	    #'Quel marché vouslez vous voir ?',
	    #('US.','Europe.', 'Japan.'))


#def USA():
    #st.markdown("USA")
    #st.sidebar.markdown("USA")
    #st.sidebar.title("Elisa")
    #st.sidebar.write("Cid")
    #st.image('')
#graphique
    #st.sidebar.line_chart(df_cars['cubicinches'])
    

#def Europe():
    #st.markdown("Europe")
    #st.sidebar.markdown("Europe")

#def Japan():
    #st.markdown("Japan")
    #st.sidebar.markdown("Japan")

#page_names_to_funcs = {
    #"USA": USA,
    #"Europe": Europe,
    #"Japan": Japan,
    }

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()

