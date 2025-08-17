#Estuduar las variables de python
myVariable = "My string Variable mal definido"
print(myVariable)
my_variable = "Mi Variable bien definido con guion bajo yen minusculas"
print(my_variable)
my_str_variable = 'My variable string bien definida 2'
print(my_str_variable)

my_bool_variable = False
print(my_bool_variable)

#Concatenar cadenas es con comas
print(myVariable, my_str_variable)

#Funcion calcular el area de un rectangulo
def cal_area_rectangulo(base, altura):
    """Calcula el are de un rectangulo"""
    area = base * altura
    return area
#Funcion imprime un mensaje
def mensaje_str(v_str):
    print(v_str)

#Llamar a las funciones declaradas

area = cal_area_rectangulo(12,4)
print(f"El area del rectangulo es : {area}")
mensaje_str("Hola Abel")

print(len(my_variable)) # Imprime el tamanio de una cadena
