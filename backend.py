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
    prompt = f"""
    You are an AI specialized in analyzing CVs for finance and accounting positions. 
    Given the following CV, provide a score from 1 to 10 based on the candidate's qualifications, 
    highlight key strengths, and suggest areas for improvement.

    CV: {cv_text}
    """
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Exemple d'utilisation
if __name__ == "__main__":
    cv_text = """Votre texte de CV ici."""
    analysis_result = analyze_cv(cv_text)
    print(analysis_result)
