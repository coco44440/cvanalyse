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
    prompt = (
        "Tu es un expert dans l'analyse de CV dans le secteur de la finance et de la comptabilité. "
        "Ta tâche est de fournir un feedback structuré et noté pour chaque CV analysé. Le feedback doit être sous forme de tableau Markdown "
        "et inclure des commentaires sur les points forts, les points faibles, le potentiel et les recommandations, "
        "ainsi que les connaissances sectorielles et réglementaires, et l'engagement professionnel.\n\n"
        "Je veux que tu me fournisses un feedback sous forme de tableau Markdown (pour chaque point une colonne) et noté pour classer les différents CV. "
        "### Contenu du feedback: #### Points Forts 1. **Formation Académique** - Diplômes pertinents dans le domaine de la finance et de la comptabilité "
        "(ex. : Master en Finance, CPA). - Institutions académiques de renom, gage de rigueur et de qualité. 2. **Expérience Professionnelle** - Solide expérience "
        "dans des entreprises reconnues, avec une progression de carrière notable. - Expériences variées incluant audit, contrôle de gestion et analyse financière, "
        "apportant une vision complète des fonctions financières. 3. **Compétences Techniques** - Maîtrise avancée d’outils financiers et comptables (Excel, ERP, "
        "logiciels de comptabilité). - Connaissance approfondie des normes IFRS et GAAP, assurant la conformité réglementaire. 4. **Réalisations Notables** - Projets "
        "ayant généré des économies significatives et améliorations des processus financiers. - Récompenses professionnelles attestant de la reconnaissance dans le "
        "secteur. #### Points Faibles 1. **Gaps dans le CV** - Quelques périodes d’inactivité non expliquées nécessitant clarification. - Changements fréquents d’emploi "
        "nécessitant une explication pour comprendre la motivation et la stabilité professionnelle. 2. **Compétences Manquantes** - Absence de certaines compétences "
        "techniques spécifiques requises pour le poste. - Manque de certaines certifications ou qualifications additionnelles pouvant être un plus. 3. **Expérience Limitée "
        "en Leadership** - Expérience limitée dans des rôles de gestion ou de leadership, ce qui pourrait être un frein pour des postes nécessitant une gestion d’équipe. "
        "#### Potentiel et Recommandations 1. **Adaptabilité et Potentiel de Croissance** - Le candidat montre une grande flexibilité et une capacité d’adaptation rapide "
        "aux nouveaux environnements. - Motivation forte pour évoluer et assumer des responsabilités supplémentaires. 2. **Formation Continue** - Encourager le candidat à "
        "poursuivre des formations continues et à acquérir des certifications additionnelles pertinentes (ex. : CFA, gestion de projet). 3. **Développement de Compétences "
        "Managériales** - Recommander des opportunités de développement de compétences en leadership et gestion d’équipe. - Participation à des programmes de mentorat interne "
        "pour préparer à des rôles de gestion. #### Connaissances Sectorielles et Réglementaires 1. **Expertise Sectorielle** - Le candidat possède une bonne compréhension "
        "des enjeux financiers spécifiques à notre secteur d’activité. - Connaissance des régulations locales et internationales, cruciales pour la conformité et la gestion "
        "des risques. 2. **Technologie et Innovation** - Participation à des projets de transformation digitale, indiquant une ouverture aux nouvelles technologies. - Expérience "
        "en sécurité des données financières, importante pour la protection des informations sensibles. #### Engagement Professionnel 1. **Réseautage et Influence** - Membre actif "
        "d’associations professionnelles, ce qui peut apporter des perspectives et des connaissances actuelles. - Publications et interventions dans des conférences, montrant une "
        "reconnaissance et une influence dans le domaine. 2. **Implication dans le Développement Professionnel** - Rôle de mentor ou coach pour des collègues juniors, démontrant une "
        "volonté de partager les connaissances et d’aider au développement des autres.\n\nCV: {cv_text}"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.5
        )
        result = response.choices[0].text.strip()
        print("Analysis result:", result)  # Debug message
        return result
    except Exception as e:
        print("Error during OpenAI API call:", str(e))  # Debug message
        return f"Erreur lors de l'appel à l'API OpenAI : {str(e)}"
