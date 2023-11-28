### Lists ###
#no hay array en python
my_list = list()
my_other_list = []

#print(len(my_list))

my_list= [20,25,35,40,24,62,52,30,30]

print(len(my_list))

my_other_list = [35, 1.74, "victor", "garcia", my_list]

print(type(my_other_list))
print(my_other_list[-1])

print(type(my_list))

age , height, name, surname, list_1 = my_other_list

print(age)

my_other_list.append("bravo")

print(my_other_list)

my_other_list.insert(2, "probando insert")
print(my_other_list)

my_other_list.remove("probando insert")
print(my_other_list)

my_other_list.insert(2, "azul")
print(my_other_list)
print(my_list)

my_pop_element = my_list.pop(0)
print(my_pop_element)
print(my_list)

#elimnar sin guardaar
del my_list[6]
print(my_list) 

print(my_list.clear())

#cambiar el valor
print(my_other_list)
my_other_list[2] = "negro"
print(my_other_list)