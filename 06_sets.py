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

#print(len(my_other_set))

#print(my_other_set[0])#TypeError: 'set' object is not subscriptable

my_other_set.add(1.74)
#print(my_other_set)

my_other_set.add("victor")#no se repite
#print(my_other_set)#no se repite

#print("victor" in my_other_set)#true
#print("brave" in my_other_set)#false) 

#delete
my_other_set.remove("victor")
print(my_other_set)

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"nodejs", "victor"}
my_set.add("uwu")
my_list = list(my_set)
print(my_set)
my_list.insert(2,"uwu")
print(type(my_list))
print(my_list)

my_set = set(my_list)
#print(my_set)

my_other_set = { "nodejs", "victor","java", "python", "nodejs",45}
print(my_other_set)
my_test_set = { 45, "nodejs"}
my_new_set = my_set.union(my_other_set)
print(my_other_set.intersection(my_set))
print(my_other_set.issuperset(my_test_set), "iwi")

print(my_test_set.issubset(my_other_set))

#pop
test_pop= my_other_set.pop()
print(test_pop)
print(my_other_set)

#remove
#si el elemento no está presenta para ser eliminado GENERA ERROR
my_other_set.remove(45)
print(my_other_set) 

#discard
#si el elemento no está presente para ser eliminado no genera error
my_other_set.discard(45)
print(my_other_set)
#print(my_new_set.difference(my_set))