import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer la clé API à partir des variables d'environnement
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("Aucune clé API fournie. Assurez-vous que le fichier .env est correctement configuré avec la clé API.")
else:
    print(f"Clé API chargée : {api_key}")

# Configuration de l'API OpenAI
openai.api_key = api_key

def analyze_cv(cv_text):
    messages = [
        {"role": "system", "content": "Tu es un expert dans l'analyse de CV dans le secteur de la finance et de la comptabilité. Ta tâche est de fournir un feedback structuré pour chaque CV analysé sous forme de tableau Markdown et de classer les CV du plus pertinent au moins pertinent. Le feedback doit inclure des commentaires sur les points forts, les points faibles et le potentiel."},
        {"role": "user", "content": f"Je veux que tu me fournisses un feedback sous forme de tableau Markdown (pour chaque point une colonne) pour classer les différents CV du plus pertinent au moins pertinent. ### Contenu du feedback: #### Points Forts 1. **Formation Académique** - Diplômes pertinents dans le domaine de la finance et de la comptabilité (ex. : Master en Finance, CPA). - Institutions académiques de renom, gage de rigueur et de qualité. 2. **Expérience Professionnelle** - Solide expérience dans des entreprises reconnues, avec une progression de carrière notable. - Expériences variées incluant audit, contrôle de gestion et analyse financière, apportant une vision complète des fonctions financières. 3. **Compétences Techniques** - Maîtrise avancée d’outils financiers et comptables (Excel, ERP, logiciels de comptabilité). - Connaissance approfondie des normes IFRS et GAAP, assurant la conformité réglementaire. 4. **Réalisations Notables** - Projets ayant généré des économies significatives et améliorations des processus financiers. - Récompenses professionnelles attestant de la reconnaissance dans le secteur. #### Points Faibles 1. **Gaps dans le CV** - Quelques périodes d’inactivité non expliquées nécessitant clarification. - Changements fréquents d’emploi nécessitant une explication pour comprendre la motivation et la stabilité professionnelle. 2. **Compétences Manquantes** - Absence de certaines compétences techniques spécifiques requises pour le poste. - Manque de certaines certifications ou qualifications additionnelles pouvant être un plus. 3. **Expérience Limitée en Leadership** - Expérience limitée dans des rôles de gestion ou de leadership, ce qui pourrait être un frein pour des postes nécessitant une gestion d’équipe. #### Potentiel 1. **Adaptabilité et Potentiel de Croissance** - Le candidat montre une grande flexibilité et une capacité d’adaptation rapide aux nouveaux environnements. - Motivation forte pour évoluer et assumer des responsabilités supplémentaires. 2. **Formation Continue** - Encourager le candidat à poursuivre des formations continues et à acquérir des certifications additionnelles pertinentes (ex. : CFA, gestion de projet). 3. **Développement de Compétences Managériales** - Recommander des opportunités de développement de compétences en leadership et gestion d’équipe. - Participation à des programmes de mentorat interne pour préparer à des rôles de gestion.\n\nCV: {cv_text}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=1000
    )
    return response.choices[0].message['content'].strip()