#De bepaling van de nummers doormiddel van input
number_1 = int(input('Typ je eerste nummer hier: '))
number_2 = int(input('Typ je tweede nummer hier: '))

#Het bepalen van de berekening
berekening = input('''
Kies de berekenings methode:
+ 
- 
* 
/ 
''')

#Het uitvoeren van de berekening
if berekening == "+":
   print(number_1, "+", number_2, "=", number_1 + number_2)

elif berekening == "-":
   print(number_1, "-", number_2, "=", number_1 + number_2)

elif berekening == "*":
   print(number_1, "*", number_2, "=", number_1 + number_2)

elif berekening == "/":
   print(number_1, "/", number_2, "=", number_1 + number_2)

#Dit wordt er verstuurd als er geen geldige input is.
else:
   print("U heeft geen geldige keuze gemaakt, begin op nieuw")