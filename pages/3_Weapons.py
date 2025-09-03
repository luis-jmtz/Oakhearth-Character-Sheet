import streamlit as st
import pandas as pd
import ast
import json

st.title("Weapons")

st.session_state.weapons = pd.read_csv(r"data\Equipment\Weapons.tsv", sep="\t")

with open('data\Equipment\weapon_dict.json', 'r') as f:
    st.session_state.dicitonary = json.load(f)

#Sets the forward dictionaries for the session
wt = st.session_state.dicitonary["type"] # weapon types
ws = st.session_state.dicitonary["styles"] #weapon styles
dt = st.session_state.dicitonary["dmg_types"] # damage types
bp = st.session_state.dicitonary["basic_properties"] # basic properties
cp = st.session_state.dicitonary["complex_properties"] # complex Properites

# reverse dictionaries
wt_rev = st.session_state.dicitonary["type_rev"]
ws_rev = st.session_state.dicitonary["styles_rev"]
dt_rev = st.session_state.dicitonary["dmg_types_rev"]
bp_rev = st.session_state.dicitonary["basic_properties_rev"]
cp_rev = st.session_state.dicitonary["complex_properties_rev"]


# Cleans Weapon types text
def dict_cleaner(dict):
    temp_list = []
    for value in dict.values():
        temp = value.replace("_", " ")
        temp_list.append(temp)

    return temp_list

st.session_state.weapon_type_list = dict_cleaner(wt)


col1, col2, col3, col4 = st.columns(4)

with col1:
    Wtype = st.selectbox(
        "Weapon Type",
        st.session_state.weapon_type_list
    )

with col2:
    Dtype = st.selectbox(
        "Damage Type",
        dt.values()
    )

with col3:
    Bproperties = st.selectbox(
        "Basic Properties",
        bp.values()
    )

with col4:
    pass


st.dataframe(st.session_state.weapons)


display_table = ""

