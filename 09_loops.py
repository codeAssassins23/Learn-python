### Loops ###
# Loops are used to iterate over a sequence of elements.

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 5
else:
    print("my_condition is greater than 10")

while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print("tiene un valor igual a 16")
        break
    print("sigue siendo menor que 20")


### FOR loops ###
my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)
else:
    print("my_list is empty")

my_tuple = (21, 1.74 , "victor" , "bravo", "victor")
for element in my_tuple:
    print(element)

my_set = { "nodejs", "victor","java", "python", "nodejs",45}
for element in my_set:
    print(element)

list_skills = ["python", "javascript", "java", "nodejs"]
my_dict = {
    'name': 'jhon',
    'apellidos':'bravo',
    'edad': 21,
    1:'python',
    2: 'javascript',
    'skills': list_skills,
    'address': {
        'street': '50',
        'number': '30',
        'zip': '12345'
    }
}
for element in my_dict.values():
    print(element)
    if element == 21:
        print("finished")
        break
else: 
    print("el bucle for para mi dict ha terminado")

for element in my_dict.values():
    print(element)
    if element == 21:
        print("finished")
        continue
    print("se ejecuta despues del continue")
else: 
    print("el bucle for para mi dict ha terminado")
