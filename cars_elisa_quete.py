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
    st.sidebar.markdown("USA")
    plt.scatter(data_frame = (df_cars[df_cars['continent'] == "US."]),
                    x="Weight_Lbs",
                    y= "Miles per gallon_(mpg)",
                    size="Weight_Lbs",
                    color="Weight_Lbs")

def page3():
    st.markdown("Japan")
    st.sidebar.markdown("Japan")
    
def page4():
    st.markdown("pays")
    st.sidebar.markdown("pays")

page_names_to_funcs = {
    "Accueil": accueil,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
    }

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


