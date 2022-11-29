import streamlit as st
import requests 
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.sidebar.header('CARS')
st.title('Vrouuuuum!! Vrouuummmm!!')


def accueil():
    
    st.sidebar.markdown('Cars')
    st.write(df_cars)
    viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

    st.pyplot(viz_correlation.figure)

    
    

def page2():
    st.markdown("USA")
    st.line_chart(df_cars['continent'].sort_values('mpg', ascending=False))
    st.write(df_cars[df_cars['continent']==' US.'])

   

    st.sidebar.markdown("Oncle Sam")

   

def page3():
    st.markdown("Japon")
    st.write(df_cars[df_cars['continent']==' Japan.'])
    st.sidebar.markdown("Soleil Levant")
    
    
def page4():
    st.markdown("Europe")
    st.write(df_cars[df_cars['continent']==' Europe.'])
    st.sidebar.markdown("Vieux Continent")

page_names_to_funcs = {
    "Accueil": accueil,
    "USA": page2,
    "Japon": page3,
    "Europe": page4,
    }

selected_page = st.sidebar.selectbox("Chosissez votre page :", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


