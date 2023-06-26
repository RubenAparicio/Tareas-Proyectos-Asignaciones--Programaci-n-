# Diseñe un programa que pida al usuario una palabra e imprima 
# por pantalla ducha palabras pero con el orden de las latras invetidos

print('\nBienvenido, este programa le permitirá visualizar') 
print('la palabra que ingrese con el orden de sus letras invertido.')

palabra = input('\nIngrese una palabra, por favor: ')
#lista vacia con las letras de la palabras
letras = []

for i in palabra:
    #llenamos nuestra lista vavia con cada una de las letras de la palabra
    letras.append(i)
    #print(letras)
#la lista de letras sale del ciclo for con todas la latras de la palabra, 
# aplicamos reverse para invertir el orden de estas letras
letras.reverse()
#print(letras)

for s in letras:
    print(s,end='')