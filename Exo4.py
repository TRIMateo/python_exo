# Créé par mateo.tripodi, le 02-12-2021 en Python 3.7
first_name = input("Quel est ton prénom? ")
last_name = input("Quel est ton nom? ")

print("Bienvenue " + first_name + " " + last_name + ".")

born_year = int(input("Quel est ton année de naissance? "))
current_year = 2021
age = current_year-born_year


print("Vu que tu es né en " + str(born_year) + ", je sais que tu as " + str(age) + " ans!")



