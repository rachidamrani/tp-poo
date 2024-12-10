class Entreprise:
    def __init__(self, nom, adresse, siret):
        # Vérification de la longueur du SIRET
        if len(str(siret)) != 14:
            raise ValueError("Le SIRET doit contenir 14 chiffres")

        self.__nom = nom
        self.__adresse = adresse
        self.__siret = siret

    def get_nom(self):
            return self.__nom

    def get_adresse(self):
        return self.__adresse

    def get_siret(self):
        return self.__siret

    def set_siret(self, nouveau_siret):
        if len(str(nouveau_siret)) != 14:
            raise ValueError("Le SIRET doit contenir !$ chiffres")

        self.__siret = nouveau_siret

    def __str__(self):
        return f"L'entreprise {self.__nom}, ayant son siège social au {self.__adresse}, possède le numéro de SIRET {self.__siret}."