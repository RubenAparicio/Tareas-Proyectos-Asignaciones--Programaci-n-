#Diseñe un porgama que compruebe que la palabra ingresada por el usuario es un palindromo o no


#la funcion recibe una palabra o frase
def comprobar_palindormo (palabras):
    # la funcion convierte las mayusculas que encuntre en minusculas
    palabras = palabras.lower()
    # La funcion reemplaza los espacios que encuentre con nada, es decir, 
    # elemina los espacios y junta las palabras en caso de haber varias
    palabras = palabras.replace (' ' , '')
    # sustituimos cualquier vocal con tile por la misma vocal sin tilde
    palabras = palabras.replace ('á' , 'a')
    palabras = palabras.replace ('é' , 'e')
    palabras = palabras.replace ('í' , 'i')
    palabras = palabras.replace ('ó' , 'o')
    palabras = palabras.replace ('ú' , 'u')
    
    #ahora si tenemos la frase o palabra de la forma correcta para hacer las comprobaciones
    
    # identificamos los indices extremos de la frase o palabra (inicio y fin)
    longitud = len(palabras)
    a = 0 
    b = longitud - 1
    
    # ciclo for que me permite recorrer la frase o palabra ingresada
    for i in range(0, longitud):
        # condicional if que compara posiciones extremas simetrica 
        # (la primera con la ultima, la segunda con la penuntila, etc) 
        # si se cumple las variables a y b van aumentando para ir 
        # acercandose al centro de la palabra o frase
        if palabras[a] == palabras[b]:
            a += 1
            b -= 1
        
        else:
                        # en caso de que la comprobacion no se cumpla 
            # se detiene y emite un mensaje
            return print('Su palabra o frase no es palindroma')
        
    # si se cumple todo el ciclo for de manera satisfactoria se emite mensaje positivo
    return print('Su palabra o frase es palindroma')        


palabras = input('\nIngrese una palabras por favor: ') 

print(comprobar_palindormo(palabras))