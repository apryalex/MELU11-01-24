import streamlit as st
from data_manager import *

def page_index_historique():
    df = email_index_rules_data
    st.header("Historique Indexation")
    st.dataframe(df)