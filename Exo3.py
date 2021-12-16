# Créé par mateo.tripodi, le 02-12-2021 en Python 3.7
first_name = input("Quel est ton prénom?")
last_name = input("Quel est ton nom?")


length_first_name = len(first_name)

reversed_first_name = first_name[length_first_name::-1]
print ("L'inverse de " + first_name + " est :",reversed_first_name)


