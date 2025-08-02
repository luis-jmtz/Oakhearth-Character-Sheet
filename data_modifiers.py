import pandas as pd

def append_ancestries(ancestry_name,size,core_traits,secondary_traits):
	path = fr"data\Ancestries.tsv"
	pass

def append_classes(class_name):
	path = fr"data\classID_Class.tsv"
	df = pd.read_csv(path,sep = '\t')

	last_id = int(df['classID'].iloc[-1])
	# print(last_id)
	new_id_value = last_id + 1

	df.loc[len(df)] = [new_id_value, class_name]
	df.to_csv("data\classID_Class.tsv", index=False,sep = '\t')
	print(df)


def append_ancestry_traits(trait_name,isCore,trait_description):
	path = fr"data\Ancestry_Traits.tsv"
	df = pd.read_csv(path,sep = '\t')

	last_id = int(df['traitID'].iloc[-1])
	# print(last_id)
	new_id_value = last_id + 1

	df.loc[len(df)] = [new_id_value, trait_name, isCore,trait_description]
	df.to_csv("data\Ancestry_Traits.tsv", index=False,sep = '\t')
	print(df)


