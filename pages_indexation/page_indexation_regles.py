import streamlit as st
from data_manager import *
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def page_index_regle():
    plot_date_distribution(data_email)
    plot_emails_by_rule(data_email)
    plot_emails_by_folder(data_email)
    plot_stacked_bar_emails_by_date(data_email)
    
    

def plot_date_distribution(data):
    st.markdown("""
    Affiche un histogramme représentant la distribution des dates d'historique des emails.""")


    

    data['DT_HISTO'] = pd.to_datetime(data['DT_HISTO'])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data['DT_HISTO'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Distribution des dates d\'historique')
    ax.set_xlabel('Date d\'historique')
    ax.set_ylabel('Nombre d\'occurrences')
    st.pyplot(fig)


def plot_emails_by_rule(data):
    st.markdown("""
    Affiche un diagramme en barres du nombre d'emails classés par règle.


    """)


    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(x='CD_RULE', data=data, palette='viridis', ax=ax)
    ax.set_title('Nombre d\'emails par règle')
    ax.set_xlabel('Règle')
    ax.set_ylabel('Nombre d\'emails')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)

def plot_emails_by_folder(data):
    st.markdown("""
    Affiche un diagramme en barres du nombre d'emails groupés par dossier d'email.


    """)


    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(x='LB_EMAIL_FOLDER', data=data, palette='muted', ax=ax)
    ax.set_title('Nombre d\'emails par dossier d\'email')
    ax.set_xlabel('Dossier d\'email')
    ax.set_ylabel('Nombre d\'emails')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)



def plot_stacked_bar_emails_by_date(data):
    st.markdown("""
    Affiche un diagramme à barres empilées du nombre d'emails traités et non traités par date d'historique.


    """)

    import matplotlib.pyplot as plt

    data['DT_HISTO'] = pd.to_datetime(data['DT_HISTO'])
    data['Traitement'] = data['CD_RULE'].apply(lambda x: 'Traité' if x != '[?]' else 'Non traité')

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(x='DT_HISTO', hue='Traitement', data=data, palette='coolwarm', ax=ax)
    ax.set_title('Nombre d\'emails traités et non traités par date')
    ax.set_xlabel('Date d\'historique')
    ax.set_ylabel('Nombre d\'emails')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)

