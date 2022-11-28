
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
	    'Quel marché vouslez vous voir ?',
	    ('US.','Europe.', 'Japan.'))
#graphique
st.line_chart(df_cars['cubicinches'])

viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

#def USA():
    #st.markdown("USA")
    #st.sidebar.markdown("USA")
    #st.sidebar.title("Elisa")
    #st.sidebar.write("Cid")
    #st.image('')

    

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
    #}

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()

