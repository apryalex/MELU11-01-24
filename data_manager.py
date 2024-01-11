    
import streamlit  as st
from datetime import datetime, timedelta
import pandas as pd

    # Afficher le bouton de rafraîchissement
# Charger les données depuis le fichier EMAIL_INDEX
data_email = pd.read_csv('data/EMAIL_INDEX.tsv', sep='\t')
# Traiter les données pour obtenir le nombre de prédictions dans chaque catégorie
counts = data_email['LB_RULE'].value_counts()

# Importer données et définition de la fonction d'actualisation des données
data_predict = pd.read_csv('data/PREDICT.tsv', sep='\t')

train_confusion_data = pd.read_csv('data/TRAIN_CONFUSION.tsv', sep='\t')

# Charger les données fusionnées depuis le fichier 'merge.tsv'
merged_data_predict = pd.read_csv('data/PREDICT.tsv', sep='\t')

email_index_rules_data = pd.read_csv('data/EMAIL_INDEX_RULES.tsv', sep='\t')




def actualiser_donnees():
      global data_predict
      
      
def bouton_actualisation_donnees():
        # date du dernier rafraîchissement
    derniere_mise_a_jour = st.empty()
    # bouton de rafraîchissement
    if st.button("Actualiser les données"):
        actualiser_donnees()
        derniere_mise_a_jour.text(f"Dernière mise à jour : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    

#SELECTION PERIODE :

# Créer une colonne pour les dates, vous pouvez remplacer cela par votre propre colonne de dates
data_predict['Date'] = pd.to_datetime(data_predict['DT_PREDICT']).dt.date

# Fonction pour filtrer les données en fonction de la période sélectionnée
def filter_data_by_period(data, selected_period):
    today = datetime.today().date()
    if selected_period == 'Dernière semaine':
        start_date = today - timedelta(days=7)
    elif selected_period == 'Dernier mois':
        start_date = today - timedelta(days=30)
    elif selected_period == '3 derniers mois':
        start_date = today - timedelta(days=90)
    elif selected_period == '6 derniers mois':
        start_date = today - timedelta(days=180)
    elif selected_period == '12 derniers mois':
        start_date = today - timedelta(days=365)
    else:
        start_date = today - timedelta(days=365)  # Par défaut, choisir la dernière année
    
    filtered_data = data[data['Date'] >= start_date]
    return filtered_data


def filter_data_by_period_pred(data, selected_period):
    today = datetime.today().date()
    if selected_period == 'Dernière semaine':
        start_date = today - timedelta(days=7)
    elif selected_period == 'Dernier mois':
        start_date = today - timedelta(days=30)
    elif selected_period == '3 derniers mois':
        start_date = today - timedelta(days=90)
    elif selected_period == '6 derniers mois':
        start_date = today - timedelta(days=180)
    elif selected_period == '12 derniers mois':
        start_date = today - timedelta(days=365)
    else:
        start_date = today - timedelta(days=365)  # Par défaut, choisir la dernière année
    
    filtered_data = data[data['DT_PREDICT'] >= start_date]
    return filtered_data
