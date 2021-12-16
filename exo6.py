print ("Bonjour cher aventurier, j'ai entendu dire que tu voulais calculer la puissance d'un nombre.")
print ("Je peux t'y aider si tu veux.")

Number = input("Quel est ce nombre ? ")
Power = input("Quelle est cette puissance ? ")
Total = int(Number)**int(Power)

print ("Mh. Je vois")
print ("Beep beep boop. . .")
print (f"La puissance {str(Power)} de {str(Number)} est {str(Total)}")
print ("Ou si tu préfères: " + str(Number) + " ^ " + str(Power) + " = " + " " + str(Total) + " 😎") 