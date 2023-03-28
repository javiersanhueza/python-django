import random

L = []

preguntas = [
    'Por qué el cielo es azul?: ',
    'Por qué hay una cara en la luna?: ',
    'Dónde están los dinosaurios?: '
]
respuesta = input(random.choice(preguntas)).strip().lower()

while respuesta != 'porque si':
    respuesta = input('Por qué?: ').strip().lower()
print('Oh, entiendo')

while len(L) < 3:
    nombre = input('Agrega un nuevo nombre: ').strip().capitalize()
    L.append(nombre)

print('Lista: ', L)
