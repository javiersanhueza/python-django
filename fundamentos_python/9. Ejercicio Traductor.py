# cerdo -> erdoCay
# apple -> appleyay

# obtener oración del usuario
original = input('Ingresa una oración: ').strip().lower()

# dividir oracion en palabras
palabras = original.split()

# recorrer palabras y convertirlas con el traductor
nuevas_palabras = []
for palabra in palabras:
    if palabra[0] in 'aeiou':
        nueva_palabra = palabra + 'yay'
        nuevas_palabras.append(nueva_palabra)
    else:
        vocal_pos = 0
        for letra in palabra:
            if letra not in 'aeiou':
                vocal_pos = vocal_pos + 1
            else:
                break
        palabra_nueva = palabra[vocal_pos:] + palabra[:vocal_pos] + 'ay'
        nuevas_palabras.append(palabra_nueva)

# unir palabras en una oracion
print(' '.join(nuevas_palabras))

# generar cadena final

