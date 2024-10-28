"""
The Magic 8 Ball es un popular juguete de oficina y juguete infantil inventado en la década de 1940 para la búsqueda de adivinos y asesoramiento. 🎱
Es una bola sobredimencionada con algunas de las siguientes respuestas:
    Sí, definitivamente.
    Es decididamente así.
    Sin duda.
    Responder brumoso, inténtalo de nuevo.
    Pregunta de nuevo más tarde.
    Mejor no te lo digas ahora.
    Mis fuentes dicen que no.
    Perspectivas no tan buena.
    Muy dudoso.

Cree un programa que pueda responder a cualquier pregunta Sí o No con una respuesta diferente cada vez que ejecute.
La salida debe tener el siguiente formato:
Pregunta:      [Pregunta]
Bola 8 magica:  [Respuesta]

Ejemplo:
Pregunta:      Es Codédex mejor que Udemy Udemy?
Bola 8 magica:  Mejor no te lo digas ahora.
"""

import random
magicNum = random.randint(1 ,9)
pregunta = input("Hazme una pregunta: ")


if magicNum == 1:
    print("Sí, definitivamente.")
elif magicNum == 2:
    print("Es decididamente así.")
elif magicNum == 3:
    print("Sin duda.")
elif magicNum == 4:
    print("Respuesta confusa, inténtalo de nuevo.")
elif magicNum == 5:
    print("Pregunta de nuevo más tarde.")
elif magicNum == 6:
    print("Mejor no te lo digo ahora.")
elif magicNum == 7:
    print("Mis fuentes dicen que no.")
elif magicNum == 8:
    print("Perspectivas no tan buena.")
elif magicNum == 9:
    print("Muy dudoso.")
