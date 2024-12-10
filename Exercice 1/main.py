from classes import *

entreprise = Entreprise("ACME Corp", "123 Rue de Paris", 12345678901234)

# Tests
print(entreprise)
print(entreprise.get_nom())

# Changement du SIRET
entreprise.set_siret(98765432109876)
print(entreprise)
