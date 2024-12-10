import random
import string
from datetime import datetime


class Client:
    def __init__(self, nom, prenom, adresse, nir):
        # Vérifications des types
        if not all(isinstance(x, str) for x in [nom, prenom, adresse]):
            raise TypeError("Nom, prénom et adresse doivent être des chaînes de caractères")

        # Vérification de la longueur du NIR
        if not isinstance(nir, (int, str)) or len(str(nir)) != 15:
            raise ValueError("Le NIR doit contenir 15 chiffres")

        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        self.__nir = str(nir)

    def get_nom(self):
        return self.__nom

class CompteBancaire:
    total_soldes = 0.0

    def __init__(self, date_creation, client, solde):
        # Vérification du type de date_creation
        if not isinstance(date_creation, str):
            raise TypeError("La date de création doit être une chaîne de caractères")

        # Vérification du type de client
        if not isinstance(client, Client):
            raise TypeError("Le client doit être une instance de la classe Client")

        # Vérification du type et de la valeur du solde
        if not isinstance(solde, (int, float)):
            raise TypeError("Le solde doit être un nombre")
        if solde < 0:
            raise ValueError("Le solde ne peut pas être négatif")

        # Conversion de la date de création
        try:
            self.__date_creation = datetime.strptime(date_creation, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Le format de date doit être 'YYYY-MM-DD'")

        self.__client = client
        self.__solde = float(solde)

        # Génération de l'identifiant interne
        lettres = ''.join(random.choices(string.ascii_uppercase, k=4))
        self.__id = f"{lettres}{self.__date_creation.strftime('%d%m%Y')}"


        # Mise à jour du solde total
        CompteBancaire.total_soldes += self.__solde

    def get_id(self):
        return self.__id

    def get_solde(self):
        return self.__solde

    def get_client(self):
        return self.__client

    # Méthode magique pour comparer les soldes
    def __eq__(self, other):
        if not isinstance(other, CompteBancaire):
            return False

        return abs(self.__solde - other.__solde) == 0

    @classmethod
    def get_total_soldes(cls):
        return cls.total_soldes