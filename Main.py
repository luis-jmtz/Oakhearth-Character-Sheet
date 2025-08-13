import streamlit as st
import json
import pandas as pd
# import os
import ast
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


# --- Choosing Ancestry --------------
st.write("### Choose an Ancestry")

ancestry_list = []
for index, row in ancestries.iterrows():
    ancestry_list.append(ancestries["Ancestry"].iloc[index])

ancestry_choice = st.selectbox(
    "",
    (ancestry_list),
)

# get ancestry ID
ancestry_row = ancestries[ancestries['Ancestry'] == ancestry_choice] # selects row
ancestry_ID = ancestry_row["ancestryID"].iloc[0] # selects column
core_traits = ast.literal_eval((ancestry_row["Core_Traits"].iloc[0]))
secondary_traits = ast.literal_eval((ancestry_row["Secondary_Traits"].iloc[0]))

# st.write(ancestry_ID)
# st.write(core_traits)
# st.write(secondary_traits)

# Display Ancestry Traits
def parse_traits(traits_list):
	output_text = ""
	for index, row in ancestry_traits.iterrows():
		if ancestry_traits["traitID"].iloc[index] in traits_list:
			trait_name = ancestry_traits["Name"].iloc[index]
			trait_descript = ancestry_traits["Description"].iloc[index]
			output_text += f"{trait_name}: {trait_descript} \n\n"
	return output_text

core_traits_text = parse_traits(core_traits)
secondary_traits_text = parse_traits(secondary_traits)


st.write("#### Core Traits")
st.write(f"{core_traits_text}")
st.write("#### Secondary Traits")
st.write(f"{secondary_traits_text}")