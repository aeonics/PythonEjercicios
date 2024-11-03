"""Desde 1927, la montaña rusa "The Cyclone" ha deleitando a los visitantes de Coney Island (Brooklyn, NY). -
Ahora están instalando un nuevo sistema de entrada (el requisito de altura es de 137 cm y el costo es de 10 créditos) y necesita su ayuda para escribir el programa para ello.


Pregúntale al usuario cuál es su altura y cuántos créditos tiene, y almacena los valores en una variable de altura y en una variable de créditos.

Utilice una combinación de operadores relacionales y lógicos para crear las reglas:

    Si son lo suficientemente altos y tienen suficientes créditos, imprime "Disfrute el paseo".
    Si tienen suficientes créditos, pero no son lo suficientemente altos, print "No eres lo suficientemente alto para montar".
    Si son lo suficientemente altos, pero no tienen suficientes créditos, imprime "No tienes suficientes créditos".
    El mismo, imprime un mensaje diciendo que no han cumplido ninguno de los requisitos."""

"""
    A	B	A and B	A or B
    False	False	False	False
    False	True	False	True
    True	False	False	True
    True	True	True	True
"""
print("Nuevo sistema de entrada para  \"The Cyclone\" ")

altura = float(input("¿Cual es tu altura en cm?: "))
creditos = int(input("¿Cuantos creditos tienes: "))



if altura >= 137 and creditos >= 10: 
    print("Disfrute el paseo")
elif altura < 137 and creditos > 10: 
    print("No eres lo suficientemente alto para montar")
elif altura >= 137 and creditos < 10:
    print ("No tienes suficientes créditos")
elif altura < 137 or creditos < 10: 
    print ("No han cumplido ninguno de los requisitos")