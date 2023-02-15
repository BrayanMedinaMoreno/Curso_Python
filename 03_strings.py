### Strings ###

my_string = "mi string"
my_other_string = "mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + "" + my_string)

my_new_line_string = "este es un string\ncon salto de linea"
print(my_new_line_string)


my_tab_string = "\teste es un string con tabulacion"
print(my_tab_string)

my_space_string = "\teste es un string \n escapado"
print(my_space_string)

# Formateo

name, surname, age = "brayan", "medina", 23

print("Mi nombre es {} {} y mi edad es {}" .format(name,surname,age))

print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))


print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Desempaquetado de paquetes

language = "python"
a,b,c,d,e,f = language

print(a)
print(b)
print(c)

# División

language_slice = language [1:3]
print(language_slice)

# Reverse

reversed_language = language [::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) # Pone la primera en mayuscula

print(language.upper()) # Todo en mayusculas

print(language.count("t")) #Cuantas 't' tiene

print(language.isnumeric()) # nos dice si es un numero

print("1".isnumeric()) # nos dice si es un numero

print(language.lower()) #todo en minusculas

print(language.upper().isupper()) #paso a mayusculas y compruebo si esta en mayusculas

print(language.startswith("py")) #empieza por 'py'







