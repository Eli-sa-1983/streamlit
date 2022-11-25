import streamlit as st
import pandas as pd


st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars

#graphique
st.line_chart(df_cars['cubicinches'])

