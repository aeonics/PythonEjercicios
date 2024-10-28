"""
En quimica, el pH es una escala que se usa para espesificar la acidez
Crea un programa que cheque cuando el niveld e pH sea basico, acido o neutral
Tip:
Crea una variable pH y pregunta al usuario un valor entre 0 y 14
Crea sentencias if, elif, else:
    Si ph es mayor que 7, escribe "Basic".
    Si ph es menor que 7, escribe  "Acidic".
    Else, escribe "Neutral".
"""

pH = int(input("Coloca un valor de 0 a 14: "))

if pH > 7:
    print("Basic")
elif pH < 7:
    print("Acidic")
else:
    print("Neutral")