### Functions ###
def my_function():
    print("Hello from a function")

my_function()

def sum_two_values(first_value, second_value):
    if(first_value == None or second_value == None):
        print("Please provide valid values")
        return
    elif(type(first_value) != int or type(second_value) != int):
        print("Please provide value integers")
        return
    result = first_value + second_value
    print(result)
number = 2
dobule_number = 2

value = sum_two_values(number, dobule_number)
print(value)

def sum_two_values_test_return(first_number, second_number):
    result = first_number + second_number
    return result

value = sum_two_values_test_return(1,2)
print(value)

def print_name(name, surname):
    print(f"My name: {name} \nMy surname:{surname}")

print_name(surname="Bravo", name="victor")

def print_name_default(name, surname, alias = "Por defecto"):
    print(f"My name: {name} \nMy surname:{surname} \nMy alias:{alias}")

print_name_default(surname="Bravo", name="victor")

def print_upper_texts(*args):
    for text in args:
        print(text.upper())

print_upper_texts("Hello", "World", "wiiii")
