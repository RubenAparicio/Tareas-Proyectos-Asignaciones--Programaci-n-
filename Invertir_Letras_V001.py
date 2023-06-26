# Diseñe un programa que pida al usuario una palabra e imprima 
# por pantalla ducha palabras pero con el orden de las latras invetidos

print('\nBienvenido, este programa le permitirá visualizar') 
print('la palabra que ingrese con el orden de sus letras invertido.')

palabra = input('\nIngrese una palabra, por favor: ')

for i in range(len(palabra)):
    # el (-i-1) indica que lo que se va a guardar 
    # en la variable v es cada una de las letras 
    # de la palabra, pero comenzando por la ultima posición 
    v = palabra[-i-1] 
    print(v,end='')
    # el comando (end='') nos ayuda a imprimir los resultados 
    # haciendo que aparezcan en una sola linea
print('\nfin')  