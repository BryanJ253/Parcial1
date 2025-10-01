edad = float(input("Ingrese su edad en años: "))
while True:
    if 0 <= edad < 13:
        print("Usted es un niño")
    elif 13 <= edad <18:
        print("Usted es un adolescente")
    elif 18 <= edad <60:
        print("Usted es un adulto") 
    elif  edad >= 60:
        print("Usted es un adulto mayor")
    else:
        print("Usted ingreso un numero negativo")
    break