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



for index, row in ancestries.iterrows():
	ancestry = ancestries["Ancestry"].iloc[index]
	st.write(f"## {ancestry}")

	size = ast.literal_eval(ancestries["Size"].iloc[index])

	size_text = parse_size(size)

	st.write(f"**Size**: {size_text}")


# for row in ancestries['Ancestry']:
# 	st.write(f"## {row}")
# 	st.write(f"Size {ancestries['Size']}")
# 	# print(row)