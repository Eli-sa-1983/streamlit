import streamlit as st
import requests 
import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt
#import plotly.express as px


st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars

#graphique
st.line_chart(df_cars['cubicinches'])

st.sidebar.title("Elisa")
st.sidebar.write("Cid")

option_velo = st.sidebar.selectbox(
	    'Quel marché vouslez vous voir ?',
	    ('US.','Europe.', 'Japan.'))

