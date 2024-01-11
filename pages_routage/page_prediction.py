import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from data_manager import *



def page_predictions():
    st.title("Prédictions Melusine")

    # Ajouter les boutons d'onglets
    onglet_selectionne = st.radio("Sélectionner un onglet", ["Synthèse", "Confusion", "Explicabilité"],key="choix_pred")

    # En fonction de l'onglet sélectionné, appeler la fonction appropriée
    if onglet_selectionne == "Synthèse":
        afficher_onglet_synthese()
    elif onglet_selectionne == "Confusion":
        afficher_onglet_confusion()
    elif onglet_selectionne == "Explicabilité":
        afficher_onglet_explicabilite()


def camembert_qualité_pred():
    # Créer le graphique camembert avec Plotly Express
    fig = px.pie(
        counts,
        names=counts.index,
        values=counts.values,
        title='Traitement des mails',
    )
    # Persnnaliser les couleurs du camembert
    fig.update_traces(marker=dict(colors=['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']))

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig)

#------------------------------------- SYNTHESE
def afficher_onglet_synthese():
   
    
    st.header("Synthèse des Prédictions")
    # Appel la fonction de préparation des données
    predictions_periode,titre_graph,  periode_selectionnee = preparation_donnees_synthese()

    bouton_actualisation_donnees()
    
    #graph prediction suivant la periode
    fig = px.bar(predictions_periode, x='DT_PREDICT', y='FL_PROBA_MAX', title=f"Prédictions pour le {periode_selectionnee} (Granularité : {'Jour' if periode_selectionnee == '3 derniers jours' else 'Mois'})")
    
    # Appeler la fonction pour le camembert avec les labels spécifiques
    selected_labels = ["Indexation manuelle dans Atlas (hors Mélusine)", "Emails archivés", "Non traité", "Autre"]
    fig_3 = camembert(data_email, 'LB_RULE', 'Repartition des mails', selected_labels)

    # Affichage des deux graphiques & explication
    st.plotly_chart(fig)
    bouton_explicatif_graph1()

    st.plotly_chart(fig_3)
    bouton_interaction_camembert()
    
    
def camembert(data, column_name, title, selected_labels=None):
    counts = data[column_name].value_counts()

    # Filtrer les labels sélectionnés et créer une nouvelle catégorie 'Autre' pour les autres
    if selected_labels is not None:
        filtered_counts = counts[counts.index.isin(selected_labels)]
    else:
        filtered_counts = counts

    autre_count = counts[~counts.index.isin(filtered_counts.index)].sum()

    # Créer un DataFrame modifié pour le graphique en camembert
    pie_data = pd.DataFrame({'label': filtered_counts.index, 'count': filtered_counts.values})
    pie_data.loc[len(pie_data)] = {'label': 'Autre', 'count': autre_count}

    fig = px.pie(pie_data, names='label', values='count', title=title)
    fig.update_traces(marker=dict(colors=['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']))
    return fig
    
def preparation_donnees_synthese():
    # Choix de la granularité (par mois ou par semaine)
    granularite_par_mois = choisir_granularite()
    # Bouton sélection de la période
    periode_selectionnee = choisir_periode()
    periodes_filtres = liste_periode_filtres()
    # Filtrage des données en fonction de la période sélectionnée
    predictions_periode = filtrer_par_periode(data_predict, periodes_filtres[periode_selectionnee])
    # Adapter la granularité des abscisses
    if granularite_par_mois == "Par semaine":
        predictions_periode['DT_PREDICT'] = pd.to_datetime(predictions_periode['DT_PREDICT'])
        titre_graph = f"Prédictions pour le {periode_selectionnee} (Granularité : Semaine)"
    else:
        # Agréger par mois ou par jour selon la période
        predictions_periode['DT_PREDICT'] = pd.to_datetime(predictions_periode['DT_PREDICT']).dt.to_period("M").astype(str)
        titre_graph = f"Prédictions pour le {periode_selectionnee} (Granularité : {'Jour' if periode_selectionnee == '3 derniers jours' else 'Mois'})"
    # Retourner les résultats nécessaires pour la fonction principale
    return predictions_periode, titre_graph, periode_selectionnee

def liste_periode_filtres():
    return {
        "3 derniers jours": (pd.to_datetime('today') - pd.DateOffset(days=2), pd.to_datetime('today')),
        "Mois en cours": ('2023-12',),  
        "3 derniers mois": ('2023-10', '2023-11', '2023-12'),
        "6 derniers mois": ('2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12'),
        "12 derniers mois": ('2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12'),
    }
    
def choisir_granularite():
  

    return st.radio("Granularité des abscisses", ["Par mois", "Par semaine"],key="granularité")

def choisir_periode():
    return st.selectbox("Sélectionner la période de prédiction", ["Mois en cours", "3 derniers mois", "6 derniers mois", "12 derniers mois", "3 derniers jours"], key="key_periode")
   
    


   
def filtrer_par_periode(data, periode):
    if isinstance(periode, int):
        today = pd.to_datetime('today').strftime('%Y-%m-%d')
        start_date = (pd.to_datetime('today') - pd.DateOffset(days=periode - 1)).strftime('%Y-%m-%d')
        return data[(data['DT_PREDICT'] >= start_date) & (data['DT_PREDICT'] <= today)]
    else:
        return data[data['DT_PREDICT'].str.startswith(periode)]




def markdown_interaction_camembert():
            st.markdown("""
    ### Interactions avec le Camembert

    Le camembert ci-dessus présente la qualité des prédictions sur toute la période. Vous pouvez interagir avec le graphique de plusieurs manières :

    - **Sélectionner/Désélectionner une catégorie :** Cliquez sur le nom de la catégorie à droite du camembert pour la sélectionner ou la désélectionner.

    - **Annuler la Sélection :** Double-cliquez sur le nom d'une catégorie pour annuler la sélection et réinitialiser le camembert.

    Profitez de ces fonctionnalités interactives pour explorer et analyser la qualité des prédictions.
    """)

def bouton_interaction_camembert():
    #Bouton pour derouler la description
    afficher_interactions_camembert = st.button("Interactions possible avec ce graphique")

    if afficher_interactions_camembert:
        markdown_interaction_camembert()
        
        afficher_contenu_markdown = st.button("Masquer l'explication")
        
        if afficher_contenu_markdown:
            markdown_interaction_camembert()
    else:
        afficher_contenu_markdown = False
        
def markdown_explicatif_graph1():
        st.markdown("""
        **Explication du Graphique :**

        Le graphique ci-dessus représente les prédictions Melusine sur une période donnée. Voici comment interpréter le graphique :

        1. **Axe des abscisses (X-axis)** : Les dates pendant la période sélectionnée.

        2. **Axe des ordonnées (Y-axis)** : Le taux de probabilité maximal (`FL_PROBA_MAX`) associé à chaque prédiction.

        3. **Ligne du graphique** : Chaque point sur la ligne du graphique représente une prédiction à une date donnée. La hauteur de la ligne à un point spécifique indique le taux de probabilité maximal associé à cette prédiction.

        Vous pouvez ajuster la période de prédiction et la granularité pour explorer comment les prédictions de Melusine varient au fil du temps.
        """)
def bouton_explicatif_graph1():
    # Bouton pour dérouler la description
    afficher_explication_graphique = st.button("Explication du graphique")

    if afficher_explication_graphique:
        markdown_explicatif_graph1()
        
        # Bouton pour masquer l'explication du graphique
        afficher_contenu_explication = st.button("Masquer l'explication")

        if afficher_contenu_explication:
            markdown_explicatif_graph1()
    else:
        afficher_contenu_explication = False



# -------------------------- MATRICE CONFUSION
def afficher_onglet_confusion():

    st.header("Matrice de Confusion")
    afficher_matrice_confusion()
    
    
def afficher_matrice_confusion():
    train_confusion_data = pd.read_csv('data/TRAIN_CONFUSION.tsv', sep='\t')
    st.subheader("Matrice de Confusion")

    # Matrice de confusion sous forme de tableau
    confusion_matrix = pd.crosstab(train_confusion_data['REAL_VALUE'], train_confusion_data['PREDICTED_VALUE'], margins=True)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(confusion_matrix, annot=True, fmt="d", ax=ax)
    plt.title("Matrice de Confusion")
    st.pyplot(fig)




# -------------------------- FIN MATRICE CONFUSION

# -------------------------- EXPLICABILITE
def afficher_onglet_explicabilite():

    st.header("Explicabilité des Prédictions")

    

# --------------------------  FIN EXPLICABILITE



# FIN PAGE PREDICTION