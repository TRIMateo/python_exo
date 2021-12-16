number1 = input("Quel est ton n1 ? " )
number2 = input("Quel est ton n2 ? " )
user_choice = input("Quel est ton choix?\n[1] Addition\n[2] Soustraction")
operator = ""
total = 0


if user_choice == "1" :
    total = int(number1) + int(number2)
    operator = "+"

if user_choice == "2" :
    total = int(number1) - int(number2)
    operator = "-"
    
print (f"Voici le résultat: {number1} {operator} {number2} = {str(total)}")
