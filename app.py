import streamlit as st
import json
import os
import ast
import sqlite3

st.title("Oakhearth Character Creator")

with open(fr'character_template.json', 'r') as file:
    char_data = json.load(file)
    # print(char_data)
    
# print(char_data["Level"])
