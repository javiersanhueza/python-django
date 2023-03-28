for numero in range(1, 11, 2):
    print(numero)

for letra in 'ABCD':
    print(letra)

vocales = 0
consonantes = 0

for letra in 'programacion':
    if letra.lower() in 'aeiou':
        vocales = vocales + 1
    elif letra == '':
        pass
    else:
        consonantes = consonantes + 1
print('vocales: ', vocales, 'consonantes: ', consonantes)

estudiantes = {
    'masculino': ['Javier', 'Theo'],
    'feminino': ['Iveth']
}

for key in estudiantes.keys():
    for nombre in estudiantes[key]:
        if 'a' in nombre:
            print(nombre, 'tiene a')

num_pares = [x for x in range(1, 101) if x % 2 == 0]
print(num_pares)

palabras = ['python', 'es', 'un', 'lenguaje', 'de', 'programación']
respuestas = [[w.upper(), w.lower(), len(w)] for w in palabras]
print(respuestas)
