"OBTENER EL FACTORIAL DE UN NUMERO CUALQUIERA"
NUM = int(input("Favor ingresar el numero para conocer su factorial: "))

def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


print(f"El factorial de {NUM} es:" )
print(factorial(NUM))

