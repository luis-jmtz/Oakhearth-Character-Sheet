import streamlit as st
import pandas as pd



ancestries = pd.read_csv(fr"data\Ancestries.tsv",sep = '\t')
ancestry_traits = pd.read_csv(fr"data\Ancestry_Traits.tsv",sep="\t")
