nuestra_lista = [27, 46, -5, 17, 99]
print(nuestra_lista)

jackson = ['A', 'B', 1, 2, 3, True, False]
print(jackson[4])
print(jackson[1:6:2])

otra_lista = [1, 2, 3, [4, 5, 6], 8]
print(otra_lista[3][0])

a = [5, 12, 71, 55, 89]
a = a + [1, 2, 3]
a = a + ['abc']
a = a + list(str(123))
a = a + list('BCD')
a.append('hola')
a.insert(2, 100)
a.insert(2, [10, 20, 30])
print(a)

# Ejemplo de uso
usuarios_conocidos = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Iveth', 'Javier', 'Theo']

while True:
    print('Hola mi nombre es Keto')
    nombre = input('Cuál es tu nombre?: ').strip().capitalize()
    if nombre in usuarios_conocidos:
        salida = 'Hola {}!'
        print(salida.format(nombre))
        eliminar = input('Te gustaría ser eliminado del sistema (y/n)?: ').strip().lower()

        if eliminar == 'y':
            usuarios_conocidos.remove(nombre)
            print(usuarios_conocidos)
        elif eliminar == 'n':
            print('No hay problema si deseas salir')
            break
    else:
        print('Mmmm no creo haberte conocido aún {}'.format(nombre))
        agregar = input('Quiere ser agregado al sistema (y/n)?: ').strip().lower()
        if agregar == 'y':
            usuarios_conocidos.append(nombre)
            print(usuarios_conocidos)
        elif agregar == 'n':
            print('No hay problema si deseas salir')
            break
