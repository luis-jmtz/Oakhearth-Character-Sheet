import pandas as pd

all_features = pd.read_csv(r"data\class_features.tsv", sep="\t")


def select_features(class_id):
	rows = all_features[all_features["classID"] == class_id]
	return rows


def load_class(class_id):
	output = select_features(class_id)
	return output

print(load_class(0))