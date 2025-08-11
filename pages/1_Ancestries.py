import streamlit as st
import pandas as pd

# ----- Load Data ---- 
st.session_state.ancestries = pd.read_csv(fr"data\Ancestries.tsv",sep = '\t')
st.session_state.ancestry_traits = pd.read_csv(fr"data\Ancestry_Traits.tsv",sep="\t")
ancestries = st.session_state.ancestries
ancestry_traits = st.session_state.ancestry_traits