import streamlit as st
import pandas as pd
import ast

# ----- Load Data ---- 
st.session_state.ancestries = pd.read_csv(fr"data\Ancestries.tsv",sep = '\t')
st.session_state.ancestry_traits = pd.read_csv(fr"data\Ancestry_Traits.tsv",sep="\t")
ancestries = st.session_state.ancestries
ancestry_traits = st.session_state.ancestry_traits

st.title("Ancestries")

def parse_size(size_list):
	size_ouput = ""

	for index in size_list:
		if size_list[index] == 0:
			size_ouput += "Medium"
			if len(size_list) > 1:
				size_ouput +=", "
		if size_list[index] == -1:
			size_ouput += "Small"

	return size_ouput

def parse_common(value):

	if value == 1:
		return "(Common)"
	else:
		return "(Uncommon)"

def parse_traits(traits_list):

	output_text = ""

	for index, row in ancestry_traits.iterrows():
		if ancestry_traits["traitID"].iloc[index] in traits_list:
			trait_name = ancestry_traits["Name"].iloc[index]
			trait_descript = ancestry_traits["Description"].iloc[index]
			output_text += f"{trait_name}: {trait_descript} \n\n"
			

	return output_text

for index, row in ancestries.iterrows():
	ancestry = ancestries["Ancestry"].iloc[index]
	
	isCommon = int(ancestries["isCommon"].iloc[index])
	isCommon = parse_common(isCommon)

	size = ast.literal_eval(ancestries["Size"].iloc[index])
	size_text = parse_size(size)

	speed = ancestries["Speed"].iloc[index]

	#--- Parse Traits ---

	core_traits = ast.literal_eval(ancestries["Core_Traits"].iloc[index])
	core_traits = parse_traits(core_traits)

	secondary_traits = ast.literal_eval(ancestries["Secondary_Traits"].iloc[index])
	secondary_traits = parse_traits(secondary_traits)

	#--- Results ----
	st.write(f"## {ancestry}")
	st.write(f"{isCommon}")
	st.markdown(f"*Size*: {size_text} \n\n*Speed*: {speed}")
	st.write("#### Core Traits")
	st.markdown(core_traits)
	st.write("#### Secondary Traits")
	st.markdown(secondary_traits)

