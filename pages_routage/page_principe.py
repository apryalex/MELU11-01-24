import streamlit as st

def page_principe():
    
    
    st.title("Bienvenue sur Melusine Manager")
    

    st.markdown("""


Melusine Manager est une plateforme puissante de gestion d'e-mails conçue par la MAIF. Cette solution open-source, développée en langage Python, repose sur des bibliothèques d'intelligence artificielle de pointe telles que Scikit Learn, TensorFlow, Keras, etc.

## Fonctionnalités Clés
Melusine excelle dans la classification intelligente des e-mails en langue française en utilisant diverses caractéristiques, dont :
- **Analyse du Corps du Mail :** Interprétation fine du texte contenu dans le corps du mail.
- **Gestion des Expéditeurs :** Identification basée sur le nom de l'expéditeur.
- **Traitement des Destinataires :** Classification en fonction des noms des destinataires.
- **Analyse Temporelle :** Prise en compte de la date de réception pour une organisation chronologique.
- **Gestion des Pièces Jointes :** Analyse de l'extension des pièces jointes.
- **Identification des Adresses E-mail :** Classification basée sur l'extension des adresses e-mail.

## Interface Conviviale
Melusine Manager offre une interface utilisateur intuitive, facilitant la gestion et l'exploration des données e-mail. Grâce à ses fonctionnalités avancées d'analyse et de visualisation, vous pourrez optimiser votre expérience de gestion des e-mails.

## Open-Source et Personnalisable
Melusine est une solution open-source, offrant une flexibilité maximale pour s'adapter à vos besoins spécifiques. Vous pouvez explorer le code source, contribuer à la communauté et personnaliser l'application selon vos exigences.

## Démarrer Avec Melusine Manager
Pour commencer à bénéficier de Melusine Manager, il vous suffit de télécharger l'application et de suivre notre guide d'installation simple. Profitez de la puissance de l'intelligence artificielle pour simplifier et améliorer la gestion de vos e-mails.

Nous vous souhaitons une expérience exceptionnelle avec Melusine Manager.
  """, unsafe_allow_html=True)