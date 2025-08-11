import streamlit as st
import json
import pandas as pd
# import os
# import ast
# import sqlite3

# st.title("Oakhearth Character Creator")

# ------- Load Data -------
ancestries = pd.read_csv(fr"data\Ancestries.tsv",sep = '\t')
ancestry_traits = pd.read_csv(fr"data\Ancestry_Traits.tsv",sep="\t")
classes = pd.read_csv(fr"data\classID_Class.tsv",sep="\t")

with open(fr'character_template.json', 'r') as file:
    char_data = json.load(file)
    # print(char_data)
