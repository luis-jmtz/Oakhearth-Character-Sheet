import streamlit as st
import pandas as pd
import ast
import json

st.title("Weapons")

weapons = pd.read_csv(r"data\Equipment\Weapons.tsv", sep="\t")

with open('data\Equipment\weapon_dict.json', 'r') as f:
    dicitonary = json.load(f)
    

types = {}
styles = {}
dmg_types = {}
basic_properties = {}
complex_properties = {}


attributes = [types, styles, dmg_types,basic_properties,complex_properties]



for key,value in dicitonary.items():    
	st.write(f"{key}, {value}")
    
         
	


col1, col2, col3, col4 = st.columns(4)

with col1:
    pass

with col2:
    pass

with col3:
    pass

with col4:
    pass


st.dataframe(weapons)


display_table = ""

