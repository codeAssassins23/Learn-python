### classes ###
# Sirve para agrupar datos y funciones que operan sobre esos datos. Ejm:
# class persson tendrá funciones solo de la clase persona


class Person:
    pass  # para que no de error de sintaxis


# Constructor: es una función que se ejecuta al crear un objeto de la clase (se llama al crear el objeto)


class MyPerson:
    def __init__(self, name, surname, alias="Sin alias"):  # this is the constructor of class MyPerson
        self.__name = name
        self.__surname = surname # __name: es una variable privada. No se puede acceder desde fuera de la clase. No se puede modificar desde fuera de la clase
        self.fullname = f"{name} {surname} {alias}"

    def walk(self):
        print(f"I'm walking. {self.fullname} has walking")

    def get_name(self): # this is a getter  
        return self.__name


# self: es una referencia al objeto que se está creando. Es como el this de java
my_person = MyPerson("Victor", "Hugo")  # this is a object of class MyPerson

print(my_person.fullname)
my_person.walk()

my_person2 = MyPerson("Victor", "Hugo", "PichuleitorPrime")
print(my_person2.fullname)
my_person2.walk()


# You can change the value of a variable of a object
my_person2.fullname = "PichuleitorPrime"
print(my_person2.fullname)
my_person2.walk()

print(my_person2.__name)  # this will give an error because __name is private