import csv
import math

def calculer_pourcentage_survie_par_classe(passagers):
    # le résultat de pourcentage de survie par classe sera stocké ici : { classe : pourcentage }
    pourcentage_par_classe = {}

    pclasses = {'1','2','3'}

    for pclass in pclasses:
        # Filtrer les passagers par classe
        passagers_pclasse = []
        
        for passager in passagers:
            if passager['pclass'] == pclass :
                passagers_pclasse.append(passager)

        # Compter le nombre de survivants dans cette classe
        passagers_survives = 0

        for passager in passagers_pclasse:
            if passager['isSurvived'] == '1':
                passagers_survives += 1

        # Calculer le pourcentage de survie dans cette classe
        total_passagers = len(passagers_pclasse)

        if total_passagers > 0:
            pourcentage_survie = (passagers_survives / total_passagers) * 100
        else:
            pourcentage_survie = 0

        # Stocker le résultat pour cette classe
        pourcentage_par_classe[pclass] = f"{round(pourcentage_survie,2)} %"

    return pourcentage_par_classe


# Pourcentage de survie par classe de passagers
with open('titanic_survival.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)

    passagers = []

    for row in reader:
        passager = {
            'pclass' : row[0].split(',')[0],
            'isSurvived':  row[0].split(',')[1]
        }

        if passager['pclass'] != '' and passager['isSurvived'] != '':
            passagers.append(passager)


    print(calculer_pourcentage_survie_par_classe(passagers))


