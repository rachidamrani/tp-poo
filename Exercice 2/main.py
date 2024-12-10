from classes import Client, CompteBancaire

try:
    # Création des clients
    client1 = Client("John", "Doe", "Montpellier", 123456789012345)
    client2 = Client("Will", "Smith", "New York", 987654321098765)
    client3 = Client("Jane", "Doe", "Paris", 127654041020765)

    # Création des comptes bancaires
    compte1 = CompteBancaire("2024-05-10", client1, 1000.50)
    compte2 = CompteBancaire("2024-01-12", client2, 1000.20)
    compte3 = CompteBancaire("2023-04-28", client3, 3200)


    print(f"Identifiant du compte 1 : { compte1.get_id() }")
    print(f"Identifiant du compte 2 : { compte2.get_id() }")

    print(f"Les comptes sont égaux : {compte1 == compte2}")
    print(f"Total des soldes bancaires : {CompteBancaire.get_total_soldes()}")

except (TypeError, ValueError) as e :
    print(f"Erreur : {e}")
