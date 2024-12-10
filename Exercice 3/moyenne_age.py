import csv
from math import floor

# Cette fonction a pour but de vérifier si une chaîne de caractères n'est pas vide et ne contient pas d'espaces vides
def is_valid_float(s):
    if s and s.strip():
        try:
            float(s)
            return True
        except ValueError:
            return False
    return False

# 1. Moyenne d'age des passagers
with open('titanic_survival.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)

    somme_age = 0.0
    moyenne_age = 0
    passagers_count = 0.0 # Compteur pour dénombrer le nombre de passagers ayant un âge valide dans le fichier CSV

    for row in reader:
        print(row)
        age = row[0].split(',')[5]

        if is_valid_float(age):
            passagers_count += 1
            somme_age += float(age)

    moyenne_age = somme_age / passagers_count

    print(floor(round(moyenne_age)))