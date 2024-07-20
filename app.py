import streamlit as st
import auth
from backend import analyze_cv
import PyPDF2
from docx import Document
import pandas as pd
import io

def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extract_text()
    return text

def read_docx(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

# Interface de connexion
def login():
    st.title('Connexion')
    username = st.text_input('Nom d\'utilisateur')
    password = st.text_input('Mot de passe', type='password')
    if st.button('Se connecter'):
        if auth.authenticate(username, password):
            st.session_state['authenticated'] = True
            st.session_state['username'] = username
        else:
            st.error('Nom d\'utilisateur ou mot de passe incorrect')

# Vérifiez l'état de l'authentification
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    login()
else:
    # Ajouter le logo de l'entreprise
    st.image("logo.png", width=150)

    st.title('Analyseur de CV pour la Finance et la Comptabilité')

    # Ajouter un message de débogage pour vérifier si le fichier est téléchargé
    st.write("Attente de téléchargement de fichiers...")

    uploaded_files = st.file_uploader("Choisissez des fichiers CV", type=["pdf", "docx", "txt"], accept_multiple_files=True)

    # Bouton pour déclencher l'analyse
    if st.button('Analyser les CVs'):
        if uploaded_files:
            cv_texts = []
            for uploaded_file in uploaded_files:
                st.write(f"Fichier {uploaded_file.name} téléchargé avec succès!")
                file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type}
                st.write(file_details)
                
                # Lire le fichier CV
                try:
                    if uploaded_file.type == "application/pdf":
                        st.write(f"Lecture du fichier PDF {uploaded_file.name}...")
                        cv_text = read_pdf(uploaded_file)
                    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                        st.write(f"Lecture du fichier DOCX {uploaded_file.name}...")
                        cv_text = read_docx(uploaded_file)
                    else:
                        st.write(f"Lecture du fichier TXT {uploaded_file.name}...")
                        cv_text = uploaded_file.read().decode("utf-8")
                    
                    # Stocker le texte du CV dans la liste
                    cv_texts.append((uploaded_file.name, cv_text))
                except Exception as e:
                    st.error(f"Une erreur est survenue lors de la lecture du fichier : {e}")
            
            # Analyser tous les CVs
            results = []
            for filename, cv_text in cv_texts:
                try:
                    st.write(f"Analyse du CV {filename} en cours...")
                    analysis_result = analyze_cv(cv_text)
                    results.append((filename, analysis_result))
                except Exception as e:
                    st.error(f"Une erreur est survenue lors de l'analyse du fichier {filename} : {e}")
            
            # Afficher les résultats après l'analyse de tous les fichiers
            for filename, result in results:
                st.subheader(f"Résultats de l'analyse pour {filename}")
                
                # Convertir le texte du tableau Markdown en un DataFrame Pandas
                try:
                    table = pd.read_csv(io.StringIO(result), sep="|", engine='python', skipinitialspace=True)
                    st.dataframe(table)
                except Exception as e:
                    st.text(result)
                    st.error(f"Erreur lors de l'affichage du tableau pour {filename} : {e}")
        else:
            st.write("Aucun fichier téléchargé.")
