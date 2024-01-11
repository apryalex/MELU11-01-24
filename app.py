import streamlit as st
import pandas as pd



#Scripts\Activate


#import pages routage
from pages_routage.page_prediction import page_predictions
from pages_routage.page_principe import page_principe
from pages_routage.page_model import page_model
from pages_routage.page_parametrage import page_parametrage

#import pages indexation
from pages_indexation.page_indexation_regles import page_index_regle
from pages_indexation.page_indexation_historique import page_index_historique
from pages_indexation.page_indexation_principe import page_index_principe


    


    
    
st.set_page_config(page_title="Melusine", page_icon="🚀", layout="wide")
def main():
    
    
    afficher_logo()
    afficher_logo_droite()
    choix_menu()
    
def choix_menu():
    # Get the selected menu
    selected_menu = st.sidebar.selectbox("Choix du Menu", ["Routage","Indexation"],key = "select_menu")

    # Call the appropriate submenu function based on the selected menu
    if selected_menu == "Routage":
        menu_routage()    
    elif selected_menu == "Indexation":
        menu_indexation()
  




def menu_indexation():
    tab1, tab2, tab3 = st.tabs(["Regles_index", "Historique_index", "Principe_index"])

    with tab1:
        
        page_index_regle()

    with tab2:
        
        page_index_historique()

    with tab3:
        page_index_principe()

def menu_routage():
    tab1, tab2, tab3, tab4 = st.tabs(["Principe", "Modèle", "Prédictions", "Paramétrage"])

    with tab1:
        
        page_principe()

    with tab2:
        
        page_model()

    with tab3:
        page_predictions()


    with tab4:
        page_predictions()

  

    






# Fonction pour afficher le logo de Melusine + CURSEUR
def afficher_logo():
    st.sidebar.image("melusine_logo.jpg", use_column_width=True)
    
    
def afficher_logo_centre():
    col1, col2, col3 = st.columns([1, 2.4, 1])
    with col2:
        st.image("melusine_logo.jpg", use_column_width=True)
        col1, col2, col3 = st.columns([1, 3, 5])
      
def afficher_logo_droite():
    col1, col2, col3 = st.columns([1, 7, 1])
    with col3:
        st.image("melusine_logo.jpg", use_column_width=True)
        


# Ajouter du CSS personnalisé
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            color: var(--theme-sidebar-textColor);
        }
    </style>
    """,
    unsafe_allow_html=True
)




###--------------------------------   MAIN + SIDEBAR






    








# Exécutez la page
if __name__ == '__main__':
    main()
