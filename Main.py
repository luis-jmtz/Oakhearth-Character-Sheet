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
st.session_state.skills = pd.read_csv(fr"data\Skills.tsv", sep="\t")
st.session_state.attribute_limit = pd.read_csv(fr"data\Attribute_Level_Limit.tsv", sep="\t")
st.session_state.prof_limit = pd.read_csv(fr"data\Proficency_Level_Limit.tsv", sep="\t")

with open(fr'character_template.json', 'r') as file:
    st.session_state.char_data = json.load(file)

# store session state data as variables
ancestries = st.session_state.ancestries
ancestry_traits = st.session_state.ancestry_traits
classes =  st.session_state.classes
character_data =  st.session_state.char_data
skills = st.session_state.skills = pd.read_csv(fr"data\Skills.tsv", sep="\t")
attribute_limit = st.session_state.attribute_limit
prof_limit = st.session_state.prof_limit


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

# ---------- Display Ancestry Traits -----------------
tcol1,tcol2 = st.columns(2,border=True)

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

with tcol1:
    st.write("#### Core Traits")
    st.write(f"{core_traits_text}")
with tcol2:
    st.write("#### Secondary Traits")
    st.write(f"{secondary_traits_text}") # choose 2 secondary traits

# ----------- Select Secondary Traits ----------------

secondary_traits_list = []
for index, row in ancestry_traits.iterrows():
    if ancestry_traits["traitID"].iloc[index] in secondary_traits:
        secondary_traits_list.append(ancestry_traits["Name"].iloc[index])

chosen1,chosen2 = st.columns(2)

chosen_secondary_traits = []

with chosen1:
    st_1 = st.selectbox(
        "Select your Two Secondary Traits",
        (secondary_traits_list),)

chosen_secondary_traits.append(st_1)
secondary_traits_list.remove(st_1)

with chosen2:
    st_2 = st.selectbox(
        "",
        (secondary_traits_list),)

chosen_secondary_traits.append(st_2)

st.warning("If a trait increases an Attribute, it cannot be increased past 3 at Character Creation")

# ------------- Define Attribute Scores -----------
might = st.session_state.mgt = 0
dexterity = st.session_state.dex = 0
intelligence = st.session_state.inte = 0
charisma = st.session_state.cha = 0
prime = st.session_state.prime = max([might, dexterity,intelligence,charisma])

base_attribute_scores = [3,1,0,-2]
remaining_attribute_scores = []


# ------------ Distribute Attribute Points -----------------
st.write("### Distribute your Attribute Points")

at_col1, at_col2, at_col3, at_col4 = st.columns(4)

with at_col1:
    at_1 = st.selectbox(
        "Might",
        (base_attribute_scores),)
    might = at_1

remaining_attribute_scores.append(at_1)
base_attribute_scores.remove(at_1)

with at_col2:
    at_2 = st.selectbox(
        "Dexterity",
        (base_attribute_scores),)
    dexterity = at_2

remaining_attribute_scores.append(at_2)
base_attribute_scores.remove(at_2)

with at_col3:
    at_3 = st.selectbox(
        "Intelligence",
        (base_attribute_scores),)
    intelligence = at_3

remaining_attribute_scores.append(at_3)
base_attribute_scores.remove(at_3)

with at_col4:
    at_4 = st.selectbox(
        "Charisma",
        (base_attribute_scores),)
    charisma = at_4

remaining_attribute_scores.append(at_4)
base_attribute_scores.remove(at_4)

# '''Add function to apply Secondary Trait bonuses to Attribute Points'''


# -------------- Increase Attribute Points ----------------
st.write("### Increase Attribute Points")
st.write("Choose which Attributes to increase")
st.write("*Note you cannot increase an Attribute Point past 3 at Character Creation")


list_of_attributes = ["Might","Dexterity","Intelligence","Charisma"]

ati_col1, ati_col2 = st.columns(2, border=True)

current_attribute_scores = [might,dexterity,intelligence,charisma]


def check_attribute_overflow():
    pass


with ati_col1:
    increase_1 = st.selectbox(
        "First Attribute Point",
        (list_of_attributes),)
    
    at_index1 = list_of_attributes.index(increase_1)
    st.write(at_index1)
    

with ati_col2:
    increase_2 = st.selectbox(
        "Second Attribute Point",
        (list_of_attributes),)


at_dis1, at_dis2, at_dis3, at_dis4 = st.columns(4)

with at_dis1:
    st.write(might)
with at_dis2:
    st.write(dexterity)
with at_dis3:
    st.write(intelligence)
with at_dis4:
    st.write(charisma)