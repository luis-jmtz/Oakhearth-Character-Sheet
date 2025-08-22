import pandas as pd
import streamlit as st

classID_dict = pd.read_csv(r"data\classID_Class.tsv", sep="\t")


def get_features(class_id):
	chosen_class = classID_dict.loc[classID_dict["classID"] == class_id] #gets the row with the chosen class
		
	class_name = chosen_class["Class"].iloc[0]

	feature_filepath = fr"data\Class_Features\{class_name}_features.tsv"
	features = pd.read_csv(feature_filepath, sep="\t")
	return(features)


def display_features_lvl1(features):
	names_list = []

	for row in features.itertuples():
		if row.Level == 1:
			names_list.append(row.Name)
	
	list_len = len(names_list)

	test = st.columns(list_len)

	for i, col in enumerate(test):
		with col:
			text = names_list[i]
			st.write(text)
			st.write(f"This is content for column {i+1}", key=i)

temp = get_features(1)

display_features_lvl1(temp)