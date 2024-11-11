"""El Sorting Hat es un sombrero mágico en la Escuela de Brujería y Magia de Hogwarts. El sombrero decide cuál de los cuatro "Casas":
    🦁 Gryffindor
    🦅 Ravenclaw
    🦡 Hufflepuff
    🐍 Slytherin

Escriba un programa que le haga algunas preguntas al usuario con las funciones de int() y input():
Q1) Te gusta Dawn o Dusk?
    1) Amanecer
    2) Dusk
    Si la respuesta es igual a 1, Gryffindor y Ravenclaw consiguen un 1 .
    Si la respuesta es igual a 2, Hufflepuff y Slytherin ambos consiguen un número 1.
    De lo contrario, descarte el mensaje "Insumo equivocado".
P2) Cuando muera, quiero que la gente me recuerde como:
    1) El Bien
    2) El Grande
    3) El sabio
    4) El audaz
    Si la respuesta es 1, Hufflepuff + 2.
    De lo contrario, si la respuesta es 2, Slytherin no.
    Si la respuesta es 3, Ravenclaw no2.
    De lo contrario, si la respuesta es 4, Gryffindor no2.
    De lo contrario, descarte el mensaje "Insumo equivocado".
Q3) Qué tipo de instrumento más complace tu oreja?
    1) El violín
    2) La trompeta
    3) El piano
    4) El tambor
    Si la respuesta es 1, Slytherin no4.
    Si la respuesta es 2, Hufflepuff no4.
    Si la respuesta es 3, Ravenclaw no4.
    De lo contrario, si la respuesta es 4, Gryffindor no4.
    Else, salida "Insumo incorrecto".
Por último, imprime la casa con más puntos."""

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

q1 = int(input("¿Te gusta el? \n 1.Amanecer \n 2.Oscuridad \n --> "))

if q1 == 1 or q1 == 2:
    Gryffindor =+ 1
    Ravenclaw =+ 1
    Hufflepuff =+ 1
    Slytherin =+ 1
else:
    print("Insumo equivocado")

q2 = int(input("Cuando muera, quiero que la gente me recuerde como: \n 1. El Bien \n 2. El Grande \n 3. El sabio \n 4. El audaz \n --> "))

if q2 == 1 or q2 == 2 or q2 == 3 or q2 == 4:
    Hufflepuff =+ 2
    Slytherin =+ 2    
    Ravenclaw =+ 2    
    Gryffindor =+ 2    
else:
    print("Insumo equivocado")

q3 = int(input("Qué tipo de instrumento más complace tu oido?: \n 1. Violin \n 2. Trompeta \n 3. Piano \n 4. Tambor \n --> "))

if q3 == 1 or q3 == 2 or q3 == 3 or q3 == 4:
    Hufflepuff =+ 4
    Slytherin =+ 4    
    Ravenclaw =+ 4    
    Gryffindor =+ 4    
else:
    print("Insumo equivocado")

print("Las puntos quedan: \n", "Gryffindor: ", Gryffindor, "\n Slytherin: ", Slytherin, "\n" , "Ravenclaw: ", Ravenclaw, "\n"  , "Gryffindor: ", Gryffindor, "\n"      )