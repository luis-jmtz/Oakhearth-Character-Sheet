import streamlit as st
import pandas as pd
import ast
import json

st.title("Weapons")

st.session_state.weapons = pd.read_csv(r"data\Equipment\Weapons.tsv", sep="\t")

display = st.session_state.weapons.drop("weaponID", axis=1)


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
    temp_list = ["-"]
    for value in dict.values():
        temp = value.replace("_", " ")
        temp_list.append(temp)

    return temp_list

st.session_state.wt_list = dict_cleaner(wt)

# Give dropdown selection boxes default values

def list_cleaner(dict):
    temp_list = ["-"]
    for value in dict.values():
        temp_list.append(value)

    return temp_list

st.session_state.ws_list = list_cleaner(ws)
st.session_state.dt_list = list_cleaner(dt)

cp_list = list_cleaner(cp)
cp_list.remove("-")

st.session_state.prop_list = list_cleaner(bp) + cp_list


col1, col2, col3, col4 = st.columns(4)

with col1:
    Wtype = st.selectbox(
        "Weapon Type",
        st.session_state.wt_list
    )

    if Wtype != "-":
        Wtype = Wtype.replace(" ", "_")

with col2:
    Stype = st.selectbox(
        "Weapon Styles",
        st.session_state.ws_list
    )

with col3:
    Dtype = st.selectbox(
        "Damage Type",
        st.session_state.dt_list
    )

with col4:
    Ptype = st.selectbox(
        "Properties",
        st.session_state.prop_list
    )






# Final Display ----------------------------------------------
for row in display.itertuples():
    st.markdown(f"#### {row.Name}")

    a,b,c,d = st.columns(4)

    with a:
        st.write(f"Styles: {row.Styles}")
    with b:
        st.write(f"Damage: {row.Damage} {row.Damage_Type}")
    with c:
        st.write(f"Properties: {row.basic_Properties} {row.complex_properties}")
    with d:
        st.write(f"Cost: {row.Cost}") 


st.dataframe(display)


