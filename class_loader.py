import pandas as pd

classID_dict = pd.read_csv(r"data\classID_Class.tsv", sep="\t")


def get_features(class_id):
	chosen_class = classID_dict.loc[classID_dict["classID"] == class_id] #gets the row with the chosen class
		
	class_name = chosen_class["Class"].iloc[0]

	feature_filepath = fr"data\Class_Features\{class_name}_features.tsv"
	features = pd.read_csv(feature_filepath, sep="\t")

	print(features)
	return(features)
	
# get_features(9)

# def select_features(class_id):
# 	rows = all_features[all_features["classID"] == class_id]
# 	return rows


# def load_class(class_id):
# 	output = select_features(class_id)
# 	return output

# print(load_class(0))