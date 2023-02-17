### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print ( type(my_dict))
print( type(my_other_dict))

my_other_dict =  {"Nombre":"brayan", "Apellido":"Medina", "Edad":21, 1:" Python"}

my_dict = {
    "Nombre":"brayan",
    "Apellido":"Medina", 
    "Edad":21, 
    "Lenguajes": {"Python","swift","kotlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

print(my_dict[1])

# Agregar
my_dict["calle"] = "calle jonia"
print(my_dict)

del my_dict["calle"]
print(my_dict)

print("brayan" in my_dict)
print("Apellido" in my_dict)


