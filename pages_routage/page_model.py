import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
from data_manager import *








###-------------------------------------------------  PAGE MODEL


def page_model():
    # Display the selected tab name at the top
    onglet_selection = onglet_page_model()

    # Afficher le titre de la page avec l'onglet sélectionné
    st.title(f"{onglet_selection}")

    # Traiter l'onglet sélectionné
    if "Contexte" in onglet_selection:
        afficher_contexte()
    elif "Historique" in onglet_selection:
        afficher_historique()
    elif "Modèle Actif" in onglet_selection:
        afficher_modele_actif()
    
    

def onglet_page_model():
    onglet_modele = st.radio("Sélectionnez un onglet", ["Contexte", "Historique", "Modèle Actif"], key = "onglet_model")
    return onglet_modele

     
# ------------- afficher_contexte
def afficher_contexte():
    
    
    st.header("Contexte du Modèle")
    st.markdown("""
        Expliquez ici le contexte dans lequel le modèle Melusine est utilisé. Cela pourrait inclure des informations sur les domaines d'application, les types de données traitées, etc.
    """)
# ------------- afficher_historique


# Afficher le DataFrame dans l'onglet Historique
def afficher_historique():
   
    # Charger les données depuis le fichier TRAIN.tsv
    df = pd.read_csv('data/TRAIN.tsv', sep='\t')
    st.header("Historique des Entraînements")
    st.dataframe(df)
    bouton_historique_entrainement()
    
def markdown_historique_entrainement():
    st.markdown("""
# Historique des Entraînements

L'historique des entraînements présente une liste chronologique des sessions d'apprentissage du modèle de prédiction des emails du dossier 'Front Office' au niveau 3. Chaque ligne correspond à une instance d'entraînement spécifique.

## Concept Clé

- **ID_TRAIN**: Identifiant unique pour chaque session d'entraînement.
- **DT_START, DT_END**: Dates de début et de fin de l'entraînement.
- **DURATION**: Durée totale de l'entraînement.
- **TEST_ACCURACY, VAL_ACCURACY**: Mesures de performance du modèle sur des jeux de test et de validation.

## Objectif

L'historique permet de suivre l'évolution des performances du modèle au fil du temps. Les détails incluent les paramètres d'entraînement, les résultats de performance et d'autres informations pertinentes.

## Utilisation

L'analyse de l'historique des entraînements aide à comprendre comment le modèle se comporte sur différentes sessions, à ajuster les paramètres pour améliorer les performances, et à prendre des décisions éclairées pour l'optimisation continue du modèle.
""")

def bouton_historique_entrainement():
    #Bouton pour derouler la description
    afficher_interactions_camembert = st.button("Explication")

    if afficher_interactions_camembert:
        markdown_historique_entrainement()
        afficher_contenu_markdown = st.button("Masquer l'explication")

        if afficher_contenu_markdown:
            markdown_historique_entrainement()

    else:
        afficher_contenu_markdown = False



# -------- afficher_modele_actif


def afficher_modele_actif():
   
    st.header("Modèle Actif")
    
    
    afficher_courbe_test_loss()
    explication_loss_test()
    
    afficher_courbe_val_loss()
    explication_loss_validation()



def afficher_courbe_test_loss():
    # Charger les données depuis le fichier TSV
    train_epochs_data = pd.read_csv('data/TRAIN_EPOCHS.tsv', sep='\t')
    st.subheader("COURBES DE LOSS")
    # Prendre seulement les 100 premières lignes
    subset_data = train_epochs_data.head(100)

    # Créer la courbe de test loss
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(subset_data['ID_EPOCH'], subset_data['TEST_LOSS'], label='Test Loss', marker='none')

    # Ajouter des labels et un titre
    ax.set_xlabel('Epochs')
    ax.set_ylabel('Test Loss')
    ax.set_title('Courbe de Test Loss pendant les Epochs')
    ax.legend()

    # Afficher la courbe
    st.pyplot(fig)



def afficher_courbe_val_loss():
    # Charger les données depuis le fichier TSV
    train_epochs_data = pd.read_csv('data/TRAIN_EPOCHS.tsv', sep='\t')
    
    # Prendre seulement les 100 premières lignes
    subset_data = train_epochs_data.head(100)

    # Créer la courbe de validation loss
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(subset_data['ID_EPOCH'], subset_data['VAL_LOSS'], label='Validation Loss', marker='none')

    # Ajouter des labels et un titre
    ax.set_xlabel('Epochs')
    ax.set_ylabel('Validation Loss')
    ax.set_title('Courbe de Validation Loss pendant les Epochs')
    ax.legend()

    # Afficher la courbe
    st.pyplot(fig) 
    
def markdown_loss_test():
        st.markdown("""
    ## Comprendre les Courbes de Test et de Validation

    Lorsque nous formons un modèle d'intelligence artificielle, comme un réseau de neurones, nous passons par plusieurs étapes appelées 'epochs'. Une epoch représente une itération complète sur l'ensemble de nos données d'entraînement.

    **Courbe de Test :**

    La courbe de test est un outil graphique qui nous aide à évaluer la performance de notre modèle au fil du temps. Elle affiche comment la 'perte' (ou erreur) de notre modèle sur un ensemble de données de test évolue à chaque epoch.

    - **L'axe des X (horizontal) :** représente les epochs, c'est-à-dire le nombre d'itérations complètes à travers les données d'entraînement.
    
    - **L'axe des Y (vertical) :** représente la perte du modèle. Plus la perte est basse, mieux le modèle fonctionne.

    **Interprétation de la Courbe de Test :**

    - Lorsque la courbe de test descend, la performance du modèle sur les données de test s'améliore.
    
    - Si la courbe monte, cela peut indiquer que le modèle a du mal à généraliser et à bien performer sur de nouvelles données.
""")
def explication_loss_test():
    #Bouton pour derouler la description
    afficher_explication_loss_test = st.button("Explication de Test loss")

    if afficher_explication_loss_test:
        markdown_loss_test()

        afficher_contenu = st.button("Masquer l'explication")

        if afficher_contenu:
            markdown_loss_test()
    else:
        afficher_contenu = False
        
        
def markdown_loss_validation():
                st.markdown("""
## Courbe de Validation

La courbe de validation évalue également la performance du modèle au fil des epochs, mais sur un ensemble de données de validation distinct qui n'a pas été utilisé pendant l'entraînement.

- Une descente de la courbe de validation suggère une bonne généralisation du modèle.

- Si la courbe de validation commence à monter alors que la courbe de test descend, cela peut indiquer un surajustement du modèle aux données d'entraînement.

*Conseil : Des courbes de test et de validation qui se stabilisent à un niveau bas sont souvent un bon indicateur de performances stables du modèle.*
""")
def explication_loss_validation():

    #Bouton pour derouler la description
    afficher_explication_loss_val = st.button("Explication de Validation loss")

    if afficher_explication_loss_val:
        markdown_loss_validation()

        afficher_contenu_markdown = st.button("Masquer l'explication")

        if afficher_contenu_markdown:
            markdown_loss_validation()
    else:
        afficher_contenu_markdown = False
# ---------------------------------------------------------------------------- FIN PAGE MODEL