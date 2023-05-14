

operaciones = {'+':"suma", '-':"resta", '*':"multiplicacion", '/':"cosiente"}

print("Bienvenido, este programa te permitira realizar las operaciones básicas entre dos números \n")
operacion = input("Inidique la operación que desea realizar ingresando su simbolo caracteristico (+,-,*,/): ")

if operaciones.get(operacion):
    
    numero_1 = input("Ingrese un primer valor:")
    print()
    numero_2 = input("Ingrese un segundo valor:")

    if operacion == "+":

        if numero_1.isnumeric() and numero_2.isnumeric():

            numero_1 = int(numero_1)
            numero_2 = int(numero_2)    
            suma = numero_1 + numero_2
            print(f"El valor de la suma es:{suma}")

        elif "." in numero_1 or "." in numero_2:

               
            numero_1 = float(numero_1)
            numero_2 = float(numero_2)

            suma = numero_1 + numero_2

            print(f"El resultado de la suma es: {suma}")
        else:
            raise ValueError ("No has ingresado un número")    
    elif operacion == "-":

        if numero_1.isnumeric() and numero_2.isnumeric():

            numero_1 = int(numero_1)
            numero_2 = int(numero_2)    
            resta = numero_1 - numero_2
            print(f"El valor de la resta es:{resta}")

        elif "." in numero_1 or "." in numero_2:

            numero_1 = float(numero_1)
            numero_2 = float(numero_2)

            resta = numero_1 - numero_2

            print(f"El resultado de la resta es: {resta}")
        else:
            raise ValueError ("No has ingresado un número")    

    elif operacion == "*":

        if numero_1.isnumeric() and numero_2.isnumeric():

            numero_1 = int(numero_1)
            numero_2 = int(numero_2)    
            producto = numero_1 * numero_2
            print(f"El valor de la multiplicacion es:{producto}")

        elif "." in numero_1 or "." in numero_2:

            numero_1 = float(numero_1)
            numero_2 = float(numero_2)

            producto = numero_1 * numero_2

            print(f"El resultado de la multiplicacion es: {producto}")
        else:
            raise ValueError ("No has ingresado un número")

    elif operacion == "/":

        if numero_1.isnumeric() and numero_2.isnumeric():

            

            numero_1 = int(numero_1)
            numero_2 = int(numero_2)    
            if numero_2 > 0 :

                cosiente = numero_1 / numero_2
                print(f"El valor de la división es:{cosiente}")
            else:
                raise ZeroDivisionError ("Recuerda que no puedes dividir entre cero")    

        elif "." in numero_1 or "." in numero_2:

            numero_1 = float(numero_1)
            numero_2 = float(numero_2)

            if numero_2 > 0:
                cosiente = numero_1 / numero_2
                print(f"El resultado de la división es: {cosiente}")
            else: 
                raise ZeroDivisionError ("Recuerda que no puedes dividir entre cero")
        else:
            raise ValueError ("No has ingredado un valor adecuado")

else: 
    raise ValueError ("No ha ingresado un simbolo adecuado, vuelve a intentarlo")