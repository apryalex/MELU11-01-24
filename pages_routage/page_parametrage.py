import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime, timedelta
from data_manager import *






    
####-------------------------------------       PAGE PARAMETRAGE

def page_parametrage():

# Fonction principale de la page de paramétragedef page_parametrage():
    st.title("Paramétrage du Modèle")

    
    # Ajouter un curseur pour le seuil de confiance
    seuil_confiance = st.slider("Seuil de Confiance",key="seuil_confiance1", min_value=0.6, max_value=1.0, value=0.8, step=0.01)
    selection_periode_param = st.selectbox("Choisissez une période", ['Dernière semaine', 'Dernier mois', '3 derniers mois', '6 derniers mois', '12 derniers mois'])

    afficher_curseur_centre()
    # Interface utilisateur Streamlit
    st.title("Sélection de période")
  

    # Filtrer les données en fonction de la période sélectionnée
    filtered_data = filter_data_by_period(data_predict, selection_periode_param)


    afficher_graphique_temps_reel(filtered_data, seuil_confiance)

    
    bouton_actualisation_donnees()


def afficher_curseur_centre():
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    
    
# Fonction pour afficher les prédictions en fonction du seuil de confiance
def afficher_predictions_avec_seuil(seuil_confiance):
    predictions_filtrees = data_predict[data_predict['FL_PROBA_MAX'] >= seuil_confiance]
    # Ajouter une colonne pour le seuil de confiance
    predictions_filtrees['Seuil_Confiance'] = seuil_confiance
    st.subheader(f"Prédictions avec seuil de confiance ≥ {seuil_confiance}")
    st.dataframe(predictions_filtrees)




# afficher le GRAPH EN TEMP REEL
# afficher le GRAPH EN TEMP REEL
def afficher_graphique_temps_reel(data, seuil_confiance):
    # Filtrer les prédictions en fonction du seuil de confiance
    predictions_filtrees = data.copy()
    predictions_filtrees['Prediction'] = predictions_filtrees['FL_PROBA_MAX'] >= seuil_confiance
    
    # Grouper les prédictions par date et calculer le taux de justesse et le taux d'erreur
    predictions_par_date = predictions_filtrees.groupby([pd.to_datetime(predictions_filtrees['DT_PREDICT']).dt.date, 'Prediction']).size().unstack(fill_value=0)
    predictions_par_date['Taux_Justesse'] = predictions_par_date[True] / (predictions_par_date[True] + predictions_par_date[False])
    predictions_par_date['Taux_Erreur'] = predictions_par_date[False] / (predictions_par_date[True] + predictions_par_date[False])

    # Afficher le graphique
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Ajouter le texte des pourcentages
    for idx, value in enumerate(predictions_par_date['Taux_Justesse']):
        plt.text(idx, value + 0.02, f'{value:.0%}', ha='center', va='bottom', color='red', fontweight='bold')

    predictions_par_date[['Taux_Justesse', 'Taux_Erreur']].plot(kind='bar', stacked=True, ax=ax, color=['red', 'lightblue'])
    plt.title(f"Taux de prédictions en fonction du seuil de confiance ({seuil_confiance:.0%})")
    plt.xlabel("Date")
    plt.ylabel("Taux de Prédictions")
    plt.ylim(0, 1)  # Limiter l'axe y entre 0 et 1 pour les taux
    plt.xticks(rotation=45, ha="right")  # Ajuster l'angle des étiquettes de l'axe x
    st.pyplot(fig)





 
def proportions_par_lb_rule(predictions_filtrees):
    # Grouper les prédictions filtrées par date et LB_RULE
    predictions_par_date_lb_rule = predictions_filtrees.groupby([pd.to_datetime(predictions_filtrees['DT_PREDICT']).dt.date, 'LB_RULE']).size().unstack(fill_value=0)

    # Calculer la distribution des LB_RULE en pourcentage
    predictions_par_date_lb_rule_percentage = predictions_par_date_lb_rule.div(predictions_par_date_lb_rule.sum(axis=1), axis=0) * 100

    return predictions_par_date_lb_rule_percentage



















    st.markdown("""
        ## Comprendre le Seuil de Confiance

        Le seuil de confiance est un paramètre important dans l'évaluation des prédictions d'un modèle d'intelligence artificielle. Il représente le niveau de certitude que le modèle doit atteindre pour qu'une prédiction soit considérée comme valide.

        #### Pourquoi le Seuil de Confiance est Important :

        Imaginez que vous développez un modèle qui prédit si un e-mail est du spam ou non. Un seuil de confiance plus élevé signifie que le modèle ne fera une prédiction que s'il est très certain que l'e-mail est du spam. À l'inverse, un seuil de confiance plus bas signifie que le modèle sera plus permissif dans ses prédictions.

        **Comment Ajuster le Seuil :**

        - Un seuil plus élevé garantit des prédictions plus précises mais peut manquer certains cas.
        
        - Un seuil plus bas peut capturer un plus grand nombre de cas, mais peut également inclure des prédictions moins fiables.

        **Exemple Simple :**

        Prenons l'exemple d'un modèle de prédiction de probabilité de pluie. Si le seuil de confiance est fixé à 80%, le modèle ne prédira qu'une chance de pluie très élevée (80% ou plus). Si vous abaissez le seuil à 50%, le modèle pourrait prédire la pluie même avec une probabilité de 50%, ce qui le rend plus sensible.

        **Conseil :** L'ajustement du seuil de confiance dépend de vos besoins spécifiques et des conséquences de fausses prédictions dans votre application.
    """)
