def table_multiplication(number):
    result = 1
    print(f"La tabla de multiplicar del numero: {number}\n")
    for i in range(0, 11 , 1):
        result = number * i
        print(f"{number} * {i} = {result}")

number = int(input("Plis provide one number: "))

table_multiplication(number)