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
	features_list = []

	for row in features.itertuples():
		if row.Level == 1:
			names_list.append(row.Name)
			
			description = row.Description
            # Split by hyphens that indicate bullet points and reformat
			description = description.replace(' - ', '\n- ')  # Add line breaks before each bullet
			description = description.replace('.   ', '.<br><br>')
			features_list.append(description)
	
	list_len = len(names_list)

	return(names_list,features_list,list_len)




temp = get_features(1)

display_features_lvl1(temp)
