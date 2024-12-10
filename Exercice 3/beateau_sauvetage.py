import csv
from collections import Counter

with open('titanic_survival.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)

    boats_with_survivors = []

    for row in reader:
        boat = row[0].split(',')[12]
        if boat != '' :
            boats_with_survivors.append(boat)


    sanitized_boats_list = []

    for boat in boats_with_survivors:
        element = boat.split()
        sanitized_boats_list.extend(element)

    count = Counter(sanitized_boats_list)

    print(f"Le bateau de sauvetage ayant sauvé le plus de passagers est le bateau numéro : {count.most_common(1)[0][0]} avec {count.most_common(2)[0][1]} passagers sauvés.")
