import random

number_random = random.randint(1,100)
print(number_random)
def advina(number_random):
    try:
        number = int(input("Plis provide one number:"))
        if number > number_random:
            print(f"EL numero es menor que {number}")
            return advina(number_random)
        elif number < number_random:
            print(f"El numero es mayor que {number}")
            return advina(number_random)
        else: 
            return f"numero adivinado: {number_random}"
    except ValueError:
        return print(f"{ValueError}")
        advina(number_random)
    
print(advina(number_random))
