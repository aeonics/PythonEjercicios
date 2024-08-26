"""Este ejemplo esta tomado de Codedex se pide
We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

    🇨🇴 Colombian pesos
    🇵🇪 Peruvian soles
    🇧🇷 Brazilian reais

Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates!"""

#Variables para tener el valor del usuario en respectivas variables
colP = 0
solP = 0
braR = 0

#Variables para cambiar los valores a dolar
usColP = 0.00025
usSolP = 0.27
usBraR = 0.18

#Variable para guardar el valor de todo
usd = 0

colP = float(input("¿Cuanto tienes en pesos colombianos: "))
solP = float(input("¿Cuanto tienes en pesos peruanos: "))
braR = float(input("¿Cuanto tienes en reales brazileños: "))


usd = ((colP * usColP) + (solP * usSolP) + (braR * usBraR))
print(usd)

