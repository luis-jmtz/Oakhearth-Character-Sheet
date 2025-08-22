import streamlit as st
import json
import pandas as pd
# import os
import ast
# import sqlite3
import class_loader

st.title("Oakhearth Character Creator")

# --------------------- Load Data ------------------
st.session_state.ancestries = pd.read_csv(fr"data\Ancestries.tsv",sep = '\t')
st.session_state.ancestry_traits = pd.read_csv(fr"data\Ancestry_Traits.tsv",sep="\t")
st.session_state.classes = pd.read_csv(fr"data\classID_Class.tsv",sep="\t")
st.session_state.skills = pd.read_csv(fr"data\Skills.tsv", sep="\t")
st.session_state.attribute_limit = pd.read_csv(fr"data\Attribute_Level_Limit.tsv", sep="\t")
st.session_state.prof_limit = pd.read_csv(fr"data\Proficency_Level_Limit.tsv", sep="\t")
st.session_state.languages = pd.read_csv(fr"data\Languages.tsv", sep="\t")

with open(fr'character_template.json', 'r') as file:
    st.session_state.char_data = json.load(file)

# store session state data as variables
ancestries = st.session_state.ancestries
ancestry_traits = st.session_state.ancestry_traits
classes =  st.session_state.classes
character_data =  st.session_state.char_data
skills = st.session_state.skills
attribute_limit = st.session_state.attribute_limit
prof_limit = st.session_state.prof_limit
languages = st.session_state.languages



# -------------------- Choosing Ancestry -----------------
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

def check_attribute_overflow(scores, index):
    temp_value = scores[index]+1

    if temp_value > 3:
        st.warning("An Attribute cannot be more than 3 at Character Creation")
    else:
        scores[index] += 1
    

with ati_col1:
    increase_1 = st.selectbox(
        "First Attribute Point",
        (list_of_attributes),)
    
    at_index1 = list_of_attributes.index(increase_1)
    check_attribute_overflow(current_attribute_scores,at_index1)
    

with ati_col2:
    increase_2 = st.selectbox(
        "Second Attribute Point",
        (list_of_attributes),)
    
    at_index2 = list_of_attributes.index(increase_2)
    check_attribute_overflow(current_attribute_scores,at_index2)


st.write("#### Your final Attribute Scores")
at_dis1, at_dis2, at_dis3, at_dis4 = st.columns(4, border=True)

might = current_attribute_scores[0]
dexterity = current_attribute_scores[1]
intelligence = current_attribute_scores[2]
charisma = current_attribute_scores[3]

prime = max(current_attribute_scores)

with at_dis1:
    st.write(f"Might: {might}")
with at_dis2:
    st.write(f"Dexterity: {dexterity}")
with at_dis3:
    st.write(f"Intelligence: {intelligence}")
with at_dis4:
    st.write(f"Charisma: {charisma}")

st.write(f"Your Prime Attribute is: {prime}")






# ------------------- Class Selection -------------------------
st.write("### Choose Your Class")

st.session_state.bonus_skill_points = 0

class_selection = st.selectbox(
    "",
    (classes["Class"]),
)

class_id = classes.loc[classes["Class"] == class_selection, "classID"].values[0]
class_data = class_loader.get_features(class_id)

names_list,features_list,list_len = class_loader.display_features_lvl1(class_data)

feature_columns = st.columns(list_len)

for i, col in enumerate(feature_columns):
    with col:
        text = names_list[i]
        st.write(f"**{text}**")
        st.markdown(features_list[i],unsafe_allow_html=True)






















# ------------ Distribute your Skill Points -----------------
st.write("### Distribute your Skill Points")
st.write("Your Starting Skill Points = 5 + Intelligence + Misc. Bonuses")

st.write("##### Skill List")
st.session_state.skill_points = 5 + intelligence + st.session_state.bonus_skill_points


def update_skill_points(number):
    st.session_state.skill_points -= number

def update_skills(skill_name, points):
    skills.loc[skills["Name"] == skill_name, "Skill_lvl"] = points
    

def gen_skills(rows, attribute):
    for index, row in rows.iterrows():

        if row["Attribute"] ==attribute:

            name = row["Name"]

            expertise = row["Expertise"]
            if expertise == 1:
                max_value = 2
            else:
                max_value = 1

            points = st.number_input(f"{name}", key=name,step=1,min_value=0,max_value=max_value)

            update_skills(name,points)
            update_skill_points(points)


sc1, sc2, sc3, remaining_points = st.columns(4)

with sc1:
    st.markdown(":gray-background[**Prime**:]")
    gen_skills(skills,5)

    st.markdown(":gray-background[**Might**:]")
    gen_skills(skills,1)

    st.markdown(":gray-background[**Dexterity**:]")
    gen_skills(skills,2)

with sc2:
    st.markdown(":gray-background[**Intelligence**:]")
    gen_skills(skills,3)

with sc3:
    st.markdown(":gray-background[**Charisma**:]")
    gen_skills(skills,4)

with remaining_points:
    st.markdown(f'''
        ##### :blue[Remaining Skill Points: {st.session_state.skill_points}]''')
    
    if st.session_state.skill_points <= 0:
        st.warning("You are out of Skill Points. Do not add anymore")



