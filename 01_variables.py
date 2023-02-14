# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print (my_bool_variable)

# Cambiar Tipo de variable

my_int_to_variable = str(my_int_variable)
print(my_int_to_variable)
print(type(my_int_to_variable))

# Imprimir variables tipo string

print (my_string_variable, my_int_variable, my_bool_variable)

# Variables en una sola linea

nombre, apellido, alias, edad = "brayan", "medina", "akari", 23

# Concatenacion de variables en un print

print("me llamo",nombre ,"mi apellido es",apellido ,"mi apodo es" ,alias, "tengo de edad", edad)
print(type(edad))

# Algunas funciones del sistema len()
print (len(my_string_variable))

# inputs
"""
first_name = input ("¿What is your name?")
edad = input("¿how old are you?")
print (first_name)
print (edad)

name = input("¿cual es tu nombre?")
age = input ("¿cuantos años tienes?")
print(name)
print(age)
"""

# Cambiamos su tipo

nombre = 23
edad = "brayan"
print(nombre)
print(edad)

# ¿forzamos el tipo? ¿tipado debil?

address: str = "mi direccion"
andress = 32
print(type(andress))
print("end")




