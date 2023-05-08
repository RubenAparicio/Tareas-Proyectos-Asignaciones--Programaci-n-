##Este Programa suma dos números
##debe emitir un mensaje al usuario cuando introduce  algo
##distinto de un numero


print("Bienvenido, este programa suma dos números\n")
num1 = input("Por favor, indique el primer número: ")
num2 = input("Por favor, indique el segundo número: ")

if num1.isnumeric() and num2.isnumeric() == True:
    Num1 = float(num1)
    Num2 = float(num2)
    suma = Num1 + Num2
    print(f"El valor de la suma es: {suma}")
else: 
    print("El valor introducido no es valido, por favor verifique para poder continuar")   