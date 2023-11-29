#### Sets ###

# Sets are unordered collections of unique elements.
# Es decir, los sets son colecciones desordenadas de elementos únicos.

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))#nos dice que inicialmente es un diccionario

my_other_set = {"victor", "bravo", 21}
print(my_other_set)
print(type(my_other_set))

print(len(my_other_set))

#print(my_other_set[0])#TypeError: 'set' object is not subscriptable

my_other_set.add(1.74)
print(my_other_set)

my_other_set.add("victor")#no se repite
print(my_other_set)#no se repite

print("victor" in my_other_set)#true
print("brave" in my_other_set)#false) 

#delete
my_other_set.remove("victor")
print(my_other_set)

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined