print ("A continuacion se le pedira que ingrese 5 numeros enteros para identificar cuales son positivos y pares")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))
num4 = int(input("Ingrese un numero: "))
num5 = int(input("Ingrese un numero: "))
suma = num1 + num2 + num3 + num4 + num5
if num1 % 2 == 0 and num1 >= 0:
    print("El numero 1 es par y positivo")
    num1 in suma
elif num1 % 2 == 0 and num1 <= 0:
    print("El numero 1 es par pero no es positivo")
else:
    print("El numero 1 no es par ni es positivo")
if num2 % 2 == 0 and num2 >= 0:
    parpositivo = True
    print("El numero 1 es par y positivo")
elif num2 % 2 == 0 and num2 <= 0:
    print("El numero 2 es par pero no es positivo")
else:
    print("El numero 2 no es par ni es positivo")
if num3 % 2 == 0 and num3 >= 0:
    parpositivo = True
    print("El numero 3 es par y positivo")
elif num3 % 2 == 0 and num3 <= 0:
    print("El numero 3 es par pero no es positivo")
else:
    print("El numero 3 no es par ni es positivo")
if num4 % 2 == 0 and num4 >= 0:
    parpositivo = True
    print("El numero 4 es par y positivo")
elif num4 % 2 == 0 and num4 <= 0:
    print("El numero 4 es par pero no es positivo")
else:
    print("El numero 4 no es par ni es positivo")
if num5 % 2 == 0 and num5 >= 0:
    parpositivo = True
    print("El numero 5 es par y positivo")
elif num5 % 2 == 0 and num5 <= 0:
    print("El numero 5 es par pero no es positivo")
else:
    print("El numero 5 no es par ni es positivo")
suma = num1 + num2 + num3 + num4 + num5
print(suma)