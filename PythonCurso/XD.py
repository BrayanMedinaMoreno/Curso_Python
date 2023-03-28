#1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("Hola Mundo")

#2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable 
#luego muestre por pantalla el contenido de la variable

Message = str("Hola Mundo")
print(type(Message))
print(Message)

#3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
#muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
Nombre = input("Introduce tu nombre: ")
print("¡Hola " + Nombre + "!")

#4 Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética  (3+22⋅5)2 .
print(((3 + 2) / (2 * 5)) ** 2)

#5 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde
horas_trabajadas = float(input("Introduce tus horas trabajadas: "))
costexHora = float(input("coste por horas trabajadas: "))
paga = horas_trabajadas * costexHora
print(paga)








##