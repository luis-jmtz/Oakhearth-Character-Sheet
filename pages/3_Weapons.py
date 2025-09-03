import streamlit as st
import pandas as pd
import ast
import json

st.title("Weapons")

st.session_state.weapons = pd.read_csv(r"data\Equipment\Weapons.tsv", sep="\t")

with open('data\Equipment\weapon_dict.json', 'r') as f:
    st.session_state.dicitonary = json.load(f)

#Sets the dictionaries for the session
weapon_types = st.session_state.dicitonary["type"]
weapon_styles = st.session_state.dicitonary["styles"]
damage_types = st.session_state.dicitonary["dmg_types"]
basic_properties = st.session_state.dicitonary["basic_properties"]
complex_properties = st.session_state.dicitonary["complex_properties"]


# Cleans Weapon types text
def dict_cleaner(dict):
    temp_list = []
    for value in dict.values():
        temp = value.replace("_", " ")
        temp_list.append(temp)

    return temp_list


st.session_state.weapon_type_list = dict_cleaner(weapon_types)


col1, col2, col3, col4 = st.columns(4)

with col1:
    Wtype = st.selectbox(
        "Weapon Type",
        st.session_state.weapon_type_list
    )

with col2:
    Dtype = st.selectbox(
        "Damage Type",
        damage_types.values()
    )

with col3:
    Bproperties = st.selectbox(
        "Basic Properties",
        basic_properties.values()
    )

with col4:
    pass


st.dataframe(st.session_state.weapons)


display_table = ""

