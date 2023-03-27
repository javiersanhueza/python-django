diccionario = {'Javier': 29, 'Iveth': 31, 'Theo': 0}
print(diccionario['Theo'])
del diccionario['Javier']
print(diccionario)
print(list(diccionario.keys()))
print(list(diccionario.values()))

familia = {
    'Javier': {'id': 'ID001', 'edad': 29},
    'Iveth': {'id': 'ID002', 'edad': 31},
    'Theo': {'id': 'ID003', 'edad': 0}
}

print(familia['Javier']['edad'])


# Ejercicio
peliculas = {
    'Nemo': {'edad': 3, 'boletos': 2},
    'Bourne': {'edad': 18, 'boletos': 5},
    'Tarzan': {'edad': 15, 'boletos': 5},
    'Spiderman': {'edad': 12, 'boletos': 5}
}

while True:
    eleccion = input('Qué película te gustaría ver?: ').strip().title()

    if eleccion in peliculas:
        edad = int(input('Cuántos años tienes?: ').strip())

        #Verificar edad del espectador
        if edad >= peliculas[eleccion]['edad']:
            # Verificar numero de boletos
            if peliculas[eleccion]['boletos'] > 0:
                peliculas[eleccion]['boletos'] = peliculas[eleccion]['boletos'] - 1
                print('Disfruta la pelicula')
            else:
                print('Ya no quedan boletos')
        else:
            print('Eres demasiado joven para ver la película')
    else:
        print('No tenemos esa película')
