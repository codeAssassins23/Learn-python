### Conditionals ###
# Conditionals are used to execute a block of code if a condition is true.+

my_condition = False

if my_condition:
    print("Is true")
else:
    print("Is false")

my_condition = "victor"

if my_condition == "jose":
    print("Is true")
else:
    print("Is false")

my_condition = None

if my_condition:
    print("Is true")

my_condition= 5*5
if my_condition >10 and my_condition < 20:
    print("entre el rango de 10 a 20")
else:
    print("no está en el rango de 10 a 20")

if my_condition >= 10 and my_condition <= 20:
    print("entre el rango de 10 a 20")
elif my_condition != 0:
    print("no es cero")

print("la ejecución continúa")

my_string = ""
if not my_string:
    print("mi cadena de texto es vacia")