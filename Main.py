import streamlit as st
import json
import pandas as pd
# import os
# import ast
# import sqlite3

st.title("Oakhearth Character Creator")

# ------- Load Data -------
st.session_state.ancestries = pd.read_csv(fr"data\Ancestries.tsv",sep = '\t')
st.session_state.ancestry_traits = pd.read_csv(fr"data\Ancestry_Traits.tsv",sep="\t")
st.session_state.classes = pd.read_csv(fr"data\classID_Class.tsv",sep="\t")
with open(fr'character_template.json', 'r') as file:
    st.session_state.char_data = json.load(file)

# store session state data as variables
ancestries = st.session_state.ancestries
ancestry_traits = st.session_state.ancestry_traits
classes =  st.session_state.classes
character_data =  st.session_state.char_data


# ------ Define Attribute Scores -------
might = st.session_state.mgt = 0
dexterity = st.session_state.dex = 0
intelligence = st.session_state.inte = 0
charisma = st.session_state.cha = 0
prime = st.session_state.prime = max([might, dexterity,intelligence,charisma])

base_attribute_scores = [3,1,0,-2]
# idea - the order of the values in the list determines what attribute the are applied to 

st.write("## Choose an Ancestry")
