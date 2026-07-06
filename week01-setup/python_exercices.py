"""
Exercices Python - Semaine 1
Objectif : consolider les bases avant d'attaquer le prompt engineering
"""

# --- Exercice 1 : conditions ---
def verifier_age(age):
    try:
        age = int(age)
    except:
        return "erreur : age invalide"

    if age < 0:
        return "erreur"
    elif age < 18:
        return "mineur"
    elif age < 65:
        return "adulte"
    else:
        return "senior"


# --- Exercice 2 : boucles + dictionnaires ---
def categoriser_notes(notes):
    excellent = 0
    bien = 0
    insuffisant = 0

    for note in notes:
        if note >= 16:
            excellent = excellent + 1
        elif note >= 12:
            bien = bien + 1
        else:
            insuffisant = insuffisant + 1

    return {"excellent": excellent, "bien": bien, "insuffisant": insuffisant}


# --- Exercice 3 : classes ---
class Note:
    def __init__(self, valeur):
        self.valeur = valeur

    def est_validee(self):
        return self.valeur >= 10


# --- Tests ---
if __name__ == "__main__":
    print(verifier_age(30))        # adulte
    print(verifier_age("vingt"))   # erreur : age invalide
    print(verifier_age(15))        # mineur

    resultats = categoriser_notes([18, 10, 14, 7, 16])
    print(f"nombre excellent = {resultats['excellent']}, nombre bien = {resultats['bien']}, nombre insuffisant = {resultats['insuffisant']}")

    n1 = Note(15)
    n2 = Note(7)
    print(n1.est_validee())  # True
    print(n2.est_validee())  # False