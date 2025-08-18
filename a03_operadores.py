#Analizaremos los operadores que soporta python.
"""
Operadores
Suma, resta, multiplicacion, division.

"""
#suma
print("La suma de 5 mas 4 :", 5 + 4)

numero1 = 10
numero2 = 5
print("La suma de 5 mas 4 version 2 :", numero1 + numero2)
resultado = numero1 + numero2
print("La suma de 5 mas 4 version 3:", resultado)

print("resultado: ", 10 + 5)
print("resultado: ", 10 - 5)
print("resultado: ", 10 * 5)
print("resultado: ", 10 % 5)
print("resultado: ", 10 // 5)
print("resultado **: ", 10 ** 3)

print("Hola"+"Python")
print("Hola"+"Python"+"Como Estas?")
print("Esto es: " + str(5))
#print("Hola" + 5)
print("Hola " *(2**3))


#-----------------------------------
# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
