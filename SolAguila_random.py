"""Simple ejemplod e uso de random, para crear un programa de Cara o cruz (sol o aguila)"""



import random

num = random.randint(0, 1)

if num  > 0.5:
  print("Sol")
else:
  print("Aguila")