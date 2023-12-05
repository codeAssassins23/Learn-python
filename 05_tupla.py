###### Tuples ######
# Tuples are immutable,es decir, no se pueden modificar ni agregar elementos
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (21, 1.74 , "victor" , "bravo", "victor")
my_other_tuple = (60,30,40,50)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[3])

uwu = my_tuple.count("victor")
print(uwu)

print(my_tuple.index("victor"))

# my_tuple[1] = 1.50 are inmutable

tuple_test = my_tuple + my_other_tuple

#print(tuple_test)

#print(tuple_test[3:6])

tuple_test = list(tuple_test)

#print(tuple_test)

tuple_test[3] = 20
tuple_test.insert(1,"azul")
tuple_test = tuple(tuple_test)
print(len(tuple_test))

#del tuple_test[0]  TypeError: 'tuple' object doesn't support item deletion

del tuple_test
#print(tuple_test) NameError