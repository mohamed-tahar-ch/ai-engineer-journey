import os
from dotenv import load_dotenv
from google import genai

# Charge la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Clé API introuvable. Vérifie ton fichier .env")

# Crée le client Gemini
client = genai.Client(api_key=api_key)

# Envoie une question au modèle
question = "Explique-moi en 2 phrases ce qu'est un AI Engineer."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)

print("Question posée :", question)
print("\nRéponse du modèle :")
print(response.text)