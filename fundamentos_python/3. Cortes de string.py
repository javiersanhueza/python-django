string = 'programacion'
print(string[4])
print(string[0:7:1])
print(string[0:7:2])
print(string[::-1])
print(string[-2])

print(string.index('aci'))
print(string.index('on'))
print(string[string.index('aci'):string.index('on')])
print(string[:string.index('cion')])

# Obtener el email del usuario
email = input('Ingresa tu correo electrónico: ').strip()

# Cortar el nombre del usuario
nombre_usuario = email[:email.index('@')]

# Cortar el dominio
dominio = email[email.index('@') + 1:]

# Mensaje de salida
salida = 'Tu nombre de usuario es {} y tu dominio es {}'
print(salida.format(nombre_usuario, dominio))

