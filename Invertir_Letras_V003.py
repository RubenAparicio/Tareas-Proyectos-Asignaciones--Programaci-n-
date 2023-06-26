# Diseñe un programa que pida al usuario una palabra e imprima 
# por pantalla ducha palabras pero con el orden de las latras invetidos

print('\nBienvenido, este programa le permitirá visualizar') 
print('la palabra que ingrese con el orden de sus letras invertido.')

palabra = input('\nIngrese una palabra, por favor: ')

n = ''
for i in palabra:
    n = i + n
print(n)
    
    