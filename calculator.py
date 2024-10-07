number_1 = int(input('Typ je eerste nummer hier: '))
number_2 = int(input('Typ je tweede nummer hier: '))

berekening = input('''
Kies de berekenings methode:
+ 
- 
* 
/ 
''')

if berekening == "+":
   print(number_1, "+", number_2, "=", number_1 + number_2)

elif berekening == "-":
   print(number_1, "-", number_2, "=", number_1 + number_2)

elif berekening == "*":
   print(number_1, "*", number_2, "=", number_1 + number_2)

elif berekening == "/":
   print(number_1, "/", number_2, "=", number_1 + number_2)

else:
   print("U heeft geen geldige keuze gemaakt, begin op nieuw")