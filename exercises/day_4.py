def factorial(number):
    fact = 1
    for i in range(1, number +1, 1):
        fact = fact * i
    return fact

number_send = int(input("PLis provide one number: "))

print(factorial(number_send))