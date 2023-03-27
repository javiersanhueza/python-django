texto = 'Happy birthday'
print(texto.count('a'))
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(texto.islower())
print(texto.isupper())
print(texto.istitle())
print(texto.isalpha())
print(texto.isdigit())
print(texto.isalnum())
print(texto.index('birthday'))
print(texto.find('birthday'))
print(texto.find('adsad'))

y = '000happy000'
print(y.strip('0'))
print(y.lstrip('0'))
print(y.rstrip('0'))


nombre = input('Cual es tu nombre: ').strip()
print(len(nombre))
